#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 430.py
@version   : 1.0
@Time      : 2019/5/23 23:03
Description about this file:

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        cur_node ,tmp_stack = head,[]
        while cur_node:
            if cur_node.child:
                if cur_node.next:
                    tmp_stack.append(cur_node.next)
                cur_node,cur_node.child.prev ,cur_node.child = cur_node.child,cur_node,None
            if not cur_node.next and len(tmp_stack):
                tmp = tmp_stack.pop()
                tmp.prev, cur_node.next = cur_node, tmp
            cur_node = cur_node.next
        return head


