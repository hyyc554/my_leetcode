"""
移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        pre_node = None
        cur_node = head
        while cur_node is not None:
            if cur_node.val == val:
                if pre_node is None:
                    head = cur_node
                else:
                    pre_node.next = cur_node.next
            else:
                pre_node = cur_node
            cur_node = cur_node.next
        return head
