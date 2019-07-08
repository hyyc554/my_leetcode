class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        index = inorder.index(preorder[0])  # 找到前序遍历结果中第一位对应在中序遍历结果中的位置
        left = inorder[0:index]
        right = inorder[index+1:]
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1+len(left)], left)
        root.right = self.buildTree(preorder[-len(right):], right)
        return root
