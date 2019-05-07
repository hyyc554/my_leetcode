#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 101.py
@version   : 1.0
@Time      : 2019/4/22 21:40
Description about this file:

"""


class Solution:
    def isSymeetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False


class Solution2:
    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])

                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True

