# https://leetcode.com/problems/freedom-trail/?envType=daily-question&envId=2024-04-27

from functools import lru_cache
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        # given a index on the ring, and target char,
        # how far direction wise is that char from the index?
        # returns array of directions to go from index
        @lru_cache(maxsize=32)
        def findMinDistanceBetween(index, char):
            ans = []

            distancesAt = []
            j = 0
            length = len(ring)

            for i in range(index, index + len(ring)):
                i = i % length
                if ring[i] == char:
                    if j <= length // 2:
                        distancesAt.append(j)
                    else:
                        distancesAt.append(j - length)
                j += 1
            return distancesAt

        def giveAbsMin(arr):
            mini = len(ring)
            ind = -1
            for i,e in enumerate(arr):
                if e == 0:
                    return 0
                if e < 0 and -1 * e < mini:
                    mini = -1*e
                    ind = i
                if e > 0 and e < mini:
                    mini = e
                    ind = i
            return arr[ind]

        @lru_cache(maxsize=32)
        def reccCall(indexOnRing, currentCharIndex):
            print(indexOnRing, key[currentCharIndex], "===")
            if currentCharIndex == len(key) - 1:
                options = findMinDistanceBetween(indexOnRing, key[currentCharIndex])
                print("we haveIOIOIO", options)
                answer = giveAbsMin(options)
                # answer = map()
                if answer >= 0:
                    return answer + 1
                else:
                    return -1 * answer + 1
            answer = []
            # print("--",findMinDistanceBetween(indexOnRing, key[currentCharIndex]))
            options = findMinDistanceBetween(indexOnRing, key[currentCharIndex])
            # print("we have", options)
            for direction in options:
                currentCost = None
                if direction < 0:
                    currentCost = direction * -1 + 1
                else:
                    currentCost = direction + 1

                # print("this",currentCost, (len(ring) + direction) % len(ring), currentCharIndex + 1)
                answer.append(currentCost + reccCall((indexOnRing + len(ring) + direction) % len(ring), currentCharIndex + 1))
            print(answer, "--", key[currentCharIndex], "%%%%%%%%%")
            print("returning", min(answer))
            return min(answer)

        finalAnswer = reccCall(0, 0)
        # print("answer", reccCall(0, 0))
        return finalAnswer


s = Solution()
print(s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"))
