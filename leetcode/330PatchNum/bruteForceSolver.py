class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        def numberToBinaryString(num):
            string = ""
            summer = 0
            counter = 0
            while num > 0:

                if num % 2 == 1:
                    string = '1' + string
                    summer += nums[counter]
                else:
                    string = '0' + string
                num = num >> 1
                counter += 1

            return [list(string), summer]

        allSums = [0] * (n+1)

        for i in range(2 ** len(nums)):
            # print(i)
            target = numberToBinaryString(i)
            print(i, target)
            if target[1] <= n:
                allSums[target[1]] = 1

        print(allSums)

        ans = 0
        for i in range(len(allSums)):
            if allSums[i] == 0:
                allSums[i] = 1
                ans += 1
                print("found one!", i)
                for j in range(len(allSums)):
                    if i != j and allSums[j] == 1 and i + j <= n:
                        allSums[i + j] = 1

        print(allSums)
        return ans
