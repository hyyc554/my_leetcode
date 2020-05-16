#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root) :
        stack = [(root,0)]
        res = []
        while stack:
            node,level = stack.pop()
            if node:
                if len(res) < level+1: # 如果是新的一层，先创建一个容器
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

# @lc code=end

