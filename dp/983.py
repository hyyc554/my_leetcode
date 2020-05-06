# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/6 20:03
@Author  : Yancy
@Email   : hyc554@gmail.com
@File    : 983.py
动态规划问题最重要是3步：

明确创建怎样的dp数组
初始化dp数组
明确动态转移方程
对于本题不难想到应该用一个数组存储到当前某一天需要花费的最少费用，这里为了下标和天数对应，dp数组的长度选择 days 中最后一个天数多加 1 个长度，因为开始没有费用，所以初始化为 0 ，之后开始对 dp 数组进行更新，那么每到达一个位置首先考虑当前天数是否在days 中，如果不在那花费的费用肯定和它前一天花费的最少费用相同(这里用一个 idx 指标指示应该处理哪一个天数，这样就不必用 if i in days 这样的语句判断天数是否需要处理了，可以让程序快一些)，如果在的话，我们就要从三种购买方式中选择一种花费费用最少的，即你想到达第 i 天，你需要从 i 的前1或7或30天的后一位置花费对应cost[0]、cost[1]、cost[2]的钱才能到第 i 天。
具

作者：LotusPanda
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/xiong-mao-shua-ti-python3-dong-tai-gui-hua-yi-do-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [ 0 for _ in range(days[-1]+1) ]
        days_index = 0
        for i in range(1,len(dp)):
            if i != days[days_index]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[max(0,i-1)]+costs[0],
                    dp[max(0,i-7)]+costs[1],
                    dp[max(0,i-30)]+costs[2],
                )
                days_index +=1
        return dp[-1]

