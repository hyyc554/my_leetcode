"""
26. 删除排序数组中的重复项
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        new_tail = 0                        # 定义一个指针变量
        for i in range(1, len(nums)):       
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]
        return new_tail+1


if __name__ == "__main__":
    sol = Solution()
    data = [1,2,2,3,3,4,4,4,4,6]
    sol.removeDuplicates(data)