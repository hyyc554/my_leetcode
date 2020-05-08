# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/8 19:29
@Author  : Yancy
@Email   : hyc554@gmail.com
@File    : 221.py

"""


class Solution:
    def maximalSquare(self, matrix) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_side = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i-1][j-1], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        max_square = max_side * max_side
        return max_square
