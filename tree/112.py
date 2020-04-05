# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        self.dfs(res,sum,root)
        return any(res)

    def dfs(self,res:list,target:int,node:TreeNode):
        if node:
            if not node.left and not node.right:
                if node.val== target:
                    res.append(True)
            if node.left:
                self.dfs(res,target-node.val,node.left)
            if node.right:
                self.dfs(res,target-node.val,node.right)


