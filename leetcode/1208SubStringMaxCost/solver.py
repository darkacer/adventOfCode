class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # def diffCalc(ch1,ch2):
        #     return ord(ch1) - ord(ch2) if ord(ch1) >= ord(ch2) else ord(ch2) - ord(ch1)
        def mod(ch1,ch2):
            return ord(ch1) - ord(ch2) if ord(ch1) >= ord(ch2) else ord(ch2) - ord(ch1)
        diffCalc = [mod(s[i],t[i]) for i in range(len(s))]

        print(diffCalc, maxCost)

        l = r = 0
        ans = r-l+1 if diffCalc[0] <= maxCost else 0
        n = len(s)
        windowCost = diffCalc[0]

        deletme = 0

        while r < n:

            if r + 1 == n or (l == r and r == n - 1):
                break

            # increment r
            peekForward = diffCalc[r + 1]
            if windowCost + peekForward <= maxCost:
                r += 1
                windowCost += peekForward

            # increment l
            else:
                removeCost = diffCalc[l]
                windowCost -= removeCost
                l += 1

            print(l,r,r-l+1, windowCost)

            ans = max(r-l+1,ans)

        print(ans,"*"*8)
        return ans


# Solution().equalSubstring("abcd","bcdf",3)
# Solution().equalSubstring("abcdef","abcdef",0)
Solution().equalSubstring("abcd","cdef",1)
# Solution().equalSubstring("abcd","acde",0)
# Solution().equalSubstring("krrgw","zjxss",19)
# Solution().equalSubstring("pxezla","loewbi",25)
