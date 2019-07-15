#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 278.py
@version   : 1.0
@Time      : 2019/5/27 22:04
Description about this file:


278. 第一个错误的版本

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。
"""


def isBadVersion(version):
    pass


class Solution:
    """
    解题思路：
    如果猜的版本为bad，那么右边界替换成当前位置
    如果猜的版本不为bad，那么左边界为当前值+1
    到最后一定是左边界为好的版本，右边界为Bad版本
    最后返回右边界
    """

    def firstBadVersion(self, n):
        low = 1
        high = n
        while low < high:
            mid = (low + high) //2
            if isBadVersion(mid) is True:
                high = mid
            else:
                low = mid + 1
        return high
