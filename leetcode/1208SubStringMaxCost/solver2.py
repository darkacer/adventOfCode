class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # def diffCalc(ch1,ch2):
        #     return ord(ch1) - ord(ch2) if ord(ch1) >= ord(ch2) else ord(ch2) - ord(ch1)
        def mod(ch1,ch2):
            return ord(ch1) - ord(ch2) if ord(ch1) >= ord(ch2) else ord(ch2) - ord(ch1)
        diffCalc = [mod(s[i],t[i]) for i in range(len(s))]

        print(diffCalc, maxCost)

        prefixArr = [0]
        acc = 0

        for i in diffCalc:
            acc += i
            prefixArr.append(acc)
        print(prefixArr)





Solution().equalSubstring("abcd","bcdf",3)
# Solution().equalSubstring("abcdef","abcdef",0)
Solution().equalSubstring("abcd","cdef",1)
# Solution().equalSubstring("abcd","acde",0)
Solution().equalSubstring("krrgw","zjxss",19)
# Solution().equalSubstring("pxezla","loewbi",25)
