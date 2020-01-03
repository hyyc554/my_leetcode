"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.



![24.jpg](https://i.loli.net/2019/12/21/tIuYraNcZvJjh8y.jpg)

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next


class Solution_with_re(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head


if __name__ == '__main__':
    from linked_list2 import SingleLinkList

    obj = SingleLinkList()
    obj.add_at_head(1)
    obj.add_at_tail(3)
    obj.add_at_index(1, 2)
    obj.add_at_index(1, 6)
    obj.travel()
    a = Solution()
    res = a.swapPairs(obj._head)
    print(res)

    # obj.travel()
