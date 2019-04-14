#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 20parent.py
@version   : 1.0
@Time      : 2019/4/14 22:23
Description about this file:

"""


class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        my_stack = []
        for i in s:
            if i not in my_dict:                                        # 如果不是反括号，入栈
                my_stack.append(i)
            elif not my_stack or my_dict[i] is not my_stack.pop():      # 如果栈为空，或者当前的反括号不能与栈尾的元素闭合
                return False
        return not my_stack                                             # 栈空则返回真，反之则假
