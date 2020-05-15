class Solution:
    def numTrees(self, n: int) -> int:
        if n ==0 or n ==1:
            return 1
        res =0
        for i in range(n):
            left_count = self.numTrees(i)
            right_count = self.numTrees(n-i-1)
            res += left_count*right_count
        return res