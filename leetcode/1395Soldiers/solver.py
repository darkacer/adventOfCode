# https://leetcode.com/problems/count-number-of-teams/
#
class Solution:

    def numTeams(self, rating):
        answer = 0

        # find numbers smaller than me
        smallersThanMe = []
        biggersThanMe = []


        for i in range(len(rating)):
            smallTempCount = 0
            bigTempCount = 0
            for j in range(0,i):
                if rating[j] < rating[i]:
                    smallTempCount += 1
                if rating[j] > rating[i]:
                    bigTempCount += 1
            smallersThanMe.append(smallTempCount)
            biggersThanMe.append(bigTempCount)

        # print(smallersThanMe)
        # print(biggersThanMe)

        # build on the basis of prev values
        lookbackArr = []
        answer = 0
        for i in range(len(rating)):
            # tempSum = 0
            for j in range(0,i):
                if rating[i] > rating[j]:
                    answer += smallersThanMe[j]
                if rating[i] < rating[j]:
                    answer += biggersThanMe[j]
            # print(answer, "here")

        print("final =", answer)
        return answer

# s = Solution().numTeams([1,3,2,4,6,5])
s = Solution().numTeams([2,1,3])
