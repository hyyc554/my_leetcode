#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 162.py
@version   : 1.0
@Time      : 2019/5/28 21:34
Description about this file:

"""


class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right
    def findPeakElement2(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    a = Solution()
    b = [1, 3, 2, 4, 5, 11, 98, 23, 48, 10, 11, 12, 13, 14]
    c = a.findPeakElement2(b)
    print(c)
