# Definition for singly-linked list..
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode):
        dummy = cur = ListNode(0)
        while head:
            if cur and cur.val > head.val:
                cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next

        return dummy.next

    def insertionSortList2(self, head):
        if not head or not head.next:
            return head
        dummpy = ListNode(0)
        


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a2.next = a1
    a3 = ListNode(6)
    a3.next = a2
    a4 = ListNode(4)
    a4.next = a3
    b = Solution().insertionSortList(a4)
