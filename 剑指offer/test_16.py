class Solution(object):
    def replaceSpaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_list = []
        for i in s:
            if i == " ":
                res_list.append("%20")
            else:
                res_list.append(i)
        return "".join(res_list)
    def replaceSpace1(self, s):
        tempstr = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

    # 简单代码替换
    # 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
    def replaceSpace2(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    # 书中给的思路
    # 判断输入类型的时候，isinstance必须首先判断，因为如果输入为integer的话，没有len，就会直接报错
    def replaceSpace3(self, s):
        if not isinstance(s,str) or len(s) <= 0 or s == None:
            return ""
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)

def test_res():
    a = Solution()
    assert a.replaceSpaces(s="hello world") == "hello%20world"
    assert a.replaceSpaces(s="") == ""
    assert a.replaceSpaces(s=" ") == "%20"
