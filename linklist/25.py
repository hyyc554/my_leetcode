# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k: int):
        """
        Use a dummy head, and

        l, r : 界定反转的头尾范围

        pre, cur : 用于反转过程，标准的链表反转方法

        jump : used to connect last node in previous k-group to first node in following k-group
        """
        dummy = jump = ListNode()
        dummy.next = l = r  = head
        while True:
            count = 0
            while r and count<k:
                r = r.next
                count +=1
            if count==k:
                pre,cur = r,l
                for _ in range(k):
                    cur.next,cur,pre = pre,cur.next,cur
                jump.next,jump,l = pre ,l,r
            else:
                return dummy.next