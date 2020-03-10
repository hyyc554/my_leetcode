"""
38. 外观数列
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。
"""

class Solution:
    def countAndSay(self, n):
        res = "1"
        for _ in range(n-1):
            res = self.helper(res)
        return res
    
    def helper(self, n):
        count, i, res = 1, 0, ""
        while i < len(n) - 1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res
