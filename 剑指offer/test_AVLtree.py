'''
题目：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，
定义其为对称的。
'''

'''
思路：如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。
先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1
34ms
6340k
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            # 返回True是因为这是最后的判断依据，在不断递归中，最后是叶子节点，即终止，如果叶子节点时，依然左右子树之差小于1，那么就是平衡二叉树，返回True
            return True
        depth1 = self.GetDepth(pRoot.left)
        depth2 = self.GetDepth(pRoot.right)
        if abs(depth1 - depth2) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def GetDepth(self, root):
        if not root:
            return 0
        return max(self.GetDepth(root.left), self.GetDepth(root.right)) + 1
