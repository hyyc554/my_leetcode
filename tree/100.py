# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return q == p
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right


# DFS iteratively
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            elif (not q or not p) or (p.val != q.val):
                return False
            stack.extend([(q.right, p.right), (q.left, p.left)])
        return True


import collections


# BFS iteratively
class Solution3:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = collections.deque([p, q])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val):
                return False
            queue.extend([(p.left, q.left), (p.right, q.right)])
        return True
