# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkNode(root,float('inf'),float("-inf"))

    def checkNode(self,node:TreeNode,max_val,min_val):
        if not node:
            return True
        if not min_val<node.val<max_val:
            return False
        return self.checkNode(node.left,node.val,min_val) and self.checkNode(node.right,max_val,node.val)


