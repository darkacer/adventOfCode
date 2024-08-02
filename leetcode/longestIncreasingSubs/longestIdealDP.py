from datetime import datetime
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        rangeMap = {}

        # this map will store the index of char when it was last time seen
        hashMap = {}
        hashMap[s[0]] = 0

        def giveLastKAlphabets(ch):
            # if ch in rangeMap:
            #     return rangeMap[ch]

            tempArr = []
            for i in range(0, k + 1):
                if (ord(ch) - i) >= 97:
                    tempArr.append(chr(ord(ch) - i))
                if (ord(ch) + i) < 123:
                    tempArr.append(chr(ord(ch) + i))
            # rangeMap[ch] = tempArr
            return tempArr

        n = len(s)

       	# Declare the list (array) for LIS and
       	# initialize LIS values for all indexes
        lis = [1]*n
        counter = 0
       	# Compute optimized LIS values in bottom up manner
        for i in range(1, n):

            for ch in giveLastKAlphabets(s[i]):
                if ch in hashMap:

                    chValue = lis[hashMap[ch]]

                    if chValue + 1 > lis[i]:
                        lis[i] = chValue + 1

            hashMap[s[i]] = i

        return max(lis)

        # return 3

s = Solution()
string = "slddedwfmoasrohdvuehfkjsfguehasxjfnrieaksmlwpruchsqeirhcjeshjfiwncoakcxnzywoajeqptycbxmzsjdi"

start_time = datetime.now()
print(s.longestIdealString(string, 3))
end_time = datetime.now()

time_difference = (end_time - start_time).total_seconds() * 10**3
print("Execution time of program is: ", time_difference, "ms")
