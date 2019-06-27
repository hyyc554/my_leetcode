class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        m = len(nums)
        startN = 1  # 列表数值范围最小值
        endN = m  # 列表数值范围最大值

        while startN <= endN:
            # midN = (startN+endN) >> 1  # 二分法中间值
            midN = (startN+endN) // 2
            numbers = 0
            for i in range(m):
                if (nums[i] <= midN) & (nums[i] >= startN):
                    numbers += 1
            # 关键(midN - startN+1)，如果没有重复元素，startN与midN范围间相差的数字个数
            if numbers > (midN - startN+1):
                startN, endN = startN, midN
            else:
                startN, endN = midN+1, endN
            if startN == endN:  # 最后判断数组出现的次数
                number = 0
                for j in nums:
                    if j == startN:
                        number += 1
                if number > 1:
                    return startN
                else:
                    break
        return False


def test_dup():
    a = Solution()
    assert a.duplicateInArray(nums=[1, 2, 2, 3, 4]) == 2
