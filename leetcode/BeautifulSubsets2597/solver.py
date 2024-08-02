# https://leetcode.com/problems/the-number-of-beautiful-subsets/?envType=daily-question&envId=2024-05-23

class Solution:
    finalAnswer = 0
    def beautifulSubsets(self, nums, k: int):
        def insertThis(pos, initArr):
            flag = True
            if not pos in pairs:
                return True
            for i in pairs[pos]:
                # if pos in pairs and i >= len(initArr):
                #     return True
                # if pos in pairs and i < len(initArr) and initArr[i] == 0:
                #     return True
                if initArr[i] == 1:
                    flag = False
                    break
            return flag

        def recc(initArr, pos):
            # print(initArr, "#$$#$")
            # print(pos)

            if len(initArr) == n:
                # print("we reached", init Arr)
                self.finalAnswer += 1
                return
            # print(pos, pairs[pos], len(initArr))
            if insertThis(pos, initArr):
                initArr.append(1)
                recc(initArr, pos+1)
                initArr.pop()

            initArr.append(0)
            recc(initArr,pos+1)
            initArr.pop()

        n = len(nums)
        nums.sort()

        totalSubSets = (1 << len(nums)) - 1
        # print(nums, n, totalSubSets)

        # find the index of pairs which cant stay togeather
        pairs = {}
        for i in range(n):
            for j in range(i,n):
                if nums[j] - nums[i] > k:
                    break
                if nums[j] - nums[i] == k:
                    # pairs.append([i,j])
                    # pairs[i] = j
                    if not j in pairs:
                        pairs[j] = []
                    pairs[j].append(i)
        # print(pairs)

        recc([],0)
        # print(self.finalAnswer - 1)
        return self.finalAnswer - 1







# Solution().beautifulSubsets([12,16,14], 2)
# Solution().beautifulSubsets([2,4,6,8,10,12,14], 2)
# Solution().beautifulSubsets([1,3], 3)
Solution().beautifulSubsets([1,1,2,3], 1)
# Solution().beautifulSubsets([2,4,6,8,10,12,14,15,16,17,18,100,103,106], 3)
# Solution().beautifulSubsets([2,6,4,8], 2)
# Solution().beautifulSubsets([2,6,4,9], 2)
# Solution().beautifulSubsets([1,3], 3)
# Solution().beautifulSubsets([2,4,6,8,10,12,14], 2) # 33
# Solution().beautifulSubsets([2,4,6,8,10,12,24], 2) # 41
# Solution().beautifulSubsets([2,4,3,5,17,19,10], 2)

# 6c6 + 6c5 + 6c4 + 6c3 + 6c2 + 6c1
# 6 + 6 + 15 + 20 + 15 + 6

# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
