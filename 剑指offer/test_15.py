class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_line = len(array) - 1
        if len_line < 1:
            return False
        len_column = len(array[0])-1
        i = 0
        j = len_column
        while i <= len_line and j >= 0:
            if array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
            else:
                return True
        return False


def test_sa():
    sa = Solution()
    assert sa.searchArray(array=[], target=2) is False
    assert sa.searchArray(array=[[1, 2, 8, 9], [2, 4, 9, 12], [
                          4, 7, 10, 13], [6, 8, 11, 15]], target=7) is True
