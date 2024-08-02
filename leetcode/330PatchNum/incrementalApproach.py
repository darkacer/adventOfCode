# doesnt work for
# nums =[1,5,10] n = 20

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        ogLen = len(nums)
        i = 0

        if nums[0] != 1:
            nums.insert(0,1)

        while True:
            prevVal = 0.5
            if i > 0:
                prevVal = nums[i - 1]

            newNum = int(prevVal * 2 + nums[i])
            print(i, prevVal, newNum, nums)

            if newNum == n:
                nums.append(newNum)
            if newNum >= n:
                break



            if i + 1 < len(nums) and nums[i + 1] > newNum:
                # print("for", i, nums[i], nums[i+1], newNum)
                # nums = nums[0:i]
                nums.insert(i + 1, newNum)

            # elif i + 1< len(nums) and nums[i + 1] <= newNum:


            elif i == len(nums) - 1:
                nums.append(newNum)

            i += 1
        # print(nums)
        return len(nums) - ogLen
