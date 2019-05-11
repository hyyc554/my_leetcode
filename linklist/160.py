class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:  # 判断特殊情况，如果两个节点中有一个为none则直接返回否
            return None
        pa, pb = headA, headB  # 创建两个节点的拷贝
        while pa is not pb:  # 如果pa不是pb
            # 假如两个节点中的任何一个，先到达了末尾，则变换已结束的节点到另一头，继续遍历
            # 如果没有遇到末尾则继续遍历
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa  # 只存在两种情况汇汇出遍历，1.两个节点相遇 2. 都到了末尾
