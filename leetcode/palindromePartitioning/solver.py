# https://leetcode.com/problems/palindrome-partitioning/description/?envType=daily-question&envId=2024-05-22
# https://assets.leetcode.com/users/images/b6f5ade4-d5b8-445e-8ee9-e16a0d4f2292_1711522213.8992066.png
# we iterate through each subsstring one by one and make sure that the array is appended
from functools import lru_cache
class Solution:
    strLen = 0
    finalAnswer = []

    @lru_cache
    def isPalindrome(self,string):
        for i in range(len(string)//2):
            # print(i)
            if string[i] != string[len(string)-i-1]:
                return False
        return True
    def _partition(self, s, pos,initArray):
        # print("new!!", pos,initArray)
        start = 0

        if pos == self.strLen:
            # print("its time to print ", initArray)
            self.finalAnswer.append([*initArray])
        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i+1]):
                initArray.append(s[start:i+1])
                self._partition(s[i+1:len(s)],pos+i+1, initArray)
                initArray.pop()

    def partition(self, s):
        self.finalAnswer = []
        self.strLen = len(s)
        self._partition(s,0,[])
        return self.finalAnswer





s = Solution()
print(s.partition("abbab"))
# print(s.partition("a"))


# s = "aaab"
# output = [["a","a","a","b"],["a","aa","b"],["aa","a","b"],["aaa","b"]]

# s = "abcaa"
# output = [["a","b","c","a","a"],["a","b","c","aa"]]

# s = "abbab"
# output = [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]

# s = "abaca"
# output = [["a","b","a","c","a"],["a","b","aca"],["aba","c","a"]]

# s = "aaa"
# output = [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]
