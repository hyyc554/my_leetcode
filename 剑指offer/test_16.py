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


def test_res():
    a = Solution()
    assert a.replaceSpaces(s="hello world") == "hello%20world"
    assert a.replaceSpaces(s="") == ""
    assert a.replaceSpaces(s=" ") == "%20"
