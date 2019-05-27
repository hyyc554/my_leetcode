#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : tmp2.py
@version   : 1.0
@Time      : 2019/5/27 21:40
Description about this file:
来自leetcode的二分查找模板2
关键属性

一种实现二分查找的高级方法。
查找条件需要访问元素的直接右邻居。
使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
保证查找空间在每一步中至少有 2 个元素。
需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。


区分语法

初始条件：left = 0, right = length
终止：left == right
向左查找：right = mid
向右查找：left = mid+1
"""


def binarySearch(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if left != len(nums) and nums[left] == target:
        return left
    return -1
