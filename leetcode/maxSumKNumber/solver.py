class Solution:
    def maxOperations(self, nums, k: int):
        hashVar = {}

        requiredVals = list(map(lambda x: k - x, nums))

        for i,e in enumerate(nums):
            if e not in hashVar:
                hashVar[e] = []
            hashVar[e].append(i)


        # print(nums, 4)
        # print(hashVar)
        # print(requiredVals)
        answer = 0

        for i,e in enumerate(requiredVals):

            if e in hashVar and len(hashVar[e]) > 0:

                index = hashVar[e].pop()
                if i >= index:
                    continue
                answer += 1
                # print(requiredVals[index], e)
                # hashVar[requiredVals[index]].pop()
                requiredVals[index] = 'x'
        print(answer)
        return answer




s = Solution()
s.maxOperations([1,2,2,3,4], 4)
s.maxOperations([3,1,3,4,3], 4)
s.maxOperations([2,2,2,3,1,1,4,1], 4)
