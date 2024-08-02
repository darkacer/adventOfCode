class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:


        numEmptyBottles = 0
        numFullBottles = numBottles
        answer = 0


        while (numFullBottles + numEmptyBottles) >= numExchange:
            print("before drink", numFullBottles, numEmptyBottles)
            # we drink all full bottles
            answer += numFullBottles

            # update number of empty bottles
            numEmptyBottles += numFullBottles
            numFullBottles = 0


            print("after drink", numFullBottles, numEmptyBottles)

            # now we get new full bottles
            numFullBottles = int(numEmptyBottles/numExchange)
            numEmptyBottles -= numFullBottles * numExchange

            print("after exchange", numFullBottles, numEmptyBottles)


        answer += numFullBottles

        return answer

s = Solution()
print("ans =",s.numWaterBottles(17,4))
