from functools import lru_cache
from math import ceil


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        @lru_cache(maxsize = 65536)
        def performDivisionAndSum(number):
            # print('for ', number)
            return sum(list(map(lambda x: ceil(x / number), nums)))

        def performBinarySearch(start, end):
            print(start, end)
            startResult = performDivisionAndSum(start)
            endResult = performDivisionAndSum(end)





        nums.sort()
        print(len(nums))

        # if performDivisionAndSum(1) <= threshold:
        #     return 1

        divisorArray = [1, *nums]

        # for i in range(1, nums[0]):
        # divisorArray.append(1)
        # for i in nums:
        #     divisorArray.append(i)

        firstLowAt = 0

        performBinarySearch(0, len(divisorArray) - 1)


        for i,e in enumerate(divisorArray):
            result = performDivisionAndSum(e)
            # print(e, result, 'result')
            if result <= threshold:
                firstLowAt = i
                print("found first low", i)
                break

        if firstLowAt < 0:
            return 1
        # print("found",firstLowAt, divisorArray[firstLowAt], divisorArray)

        # print("running loop", divisorArray[firstLowAt - 1], divisorArray[firstLowAt])
        for x in range(divisorArray[firstLowAt - 1], divisorArray[firstLowAt]):
            result = performDivisionAndSum(x)
            # print(x, result)
            if result <= threshold:
                return x



        return divisorArray[firstLowAt]


s = Solution()
print("answer", s.smallestDivisor([1,2,5,9],6))
