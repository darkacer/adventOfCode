# https://leetcode.com/problems/longest-ideal-subsequence/description/?envType=daily-question&envId=2024-04-25
#
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        def isInRange(ch1, ch2):
            return max(ord(ch1), ord(ch2)) - min(ord(ch1), ord(ch2)) <= k


        # Binary search approach
        n = len(s)
        ans = []

        # Initialize the answer list with the
        # first element of nums
        ans.append(s[0])

        for i in range(1, n):
            print(ans, ans[-1], s[i])
            if isInRange(s[i], ans[-1]):
                # If the current number is greater
                # than the last element of the answer
                # list, it means we have found a
                # longer increasing subsequence.
                # Hence, we append the current number
                # to the answer list.
                ans.append(s[i])
            else:
                # If the current number is not
                # greater than the last element of
                # the answer list, we perform
                # a binary search to find the smallest
                # element in the answer list that
                # is greater than or equal to the
                # current number.
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if isInRange(ans[mid], s[i]):
                        low = mid + 1
                    else:
                        high = mid
                # We update the element at the
                # found position with the current number.
                # By doing this, we are maintaining
                # a sorted order in the answer list.
                ans[low] = s[i]

        # The length of the answer list
        # represents the length of the
        # longest increasing subsequence.
        print(ans)
        return len(ans)

sol = Solution()
print(sol.longestIdealString("acfgbd", 2))
