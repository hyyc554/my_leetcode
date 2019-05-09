class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            out_pair = self.isMirror(left.left, right.right)
            in_pair = self.isMirror(left.right, right.left)
            return out_pair and in_pair
        else:
            return False

    def isSymeetric(self, root):
        """
        递归法
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
