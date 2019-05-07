#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 33.py
@version   : 1.0
@Time      : 2019/4/16 21:35
Description about this file:

"""


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:                  # 当前全序列已经是正序
                if nums[low] <= target <= nums[mid]:    # 目标值在最低值与中间值之间
                    high = mid - 1                      # 最高索引变为中间值-1位
                else:                                   # 目标值在中间值与最高值之间
                    low = mid + 1                       # 最低索引变为中间索引+1
            else:                                       # 当前序列存在反序列
                if nums[mid] <= target <= nums[high]:   # 目标值在中间值与最高值之间
                    low = mid + 1                       # 最低索引变为中间值+1位

                else:                                   # 目标值在最低值与中间值之间
                    high = mid - 1                      # 最高索引变为中间值-1位
        return -1


if __name__ == '__main__':
    a = Solution()
    nums = [9,8,2,3,4,6,7]
    target = 3
    b =a.search(nums,target)
    print(b)


    def get_most_similar_fast(self, v):
        scores = self.normed(v) @ self.embs._normalized_matrix.T
        scores = (scores + 1) / 2
        return scores
