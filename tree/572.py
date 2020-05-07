# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/7 19:48
@Author  : Yancy
@Email   : hyc554@gmail.com
@File    : 572.py

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, big_tree: TreeNode, small_tree: TreeNode):
        if not big_tree and not small_tree:
            return True
        if not (big_tree and small_tree):
            return False
        if big_tree.val != small_tree.val:
            return False
        return self.isSameTree(big_tree.left, small_tree.left) and self.isSameTree(big_tree.right, small_tree.right)
