class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

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


        hashMap = {}

        center = len(ring) // 2

        hashMap[ring[0]] = [0]
        # count = 1
        for i in range(1,len(ring)//2 + 1):
            if ring[i] not in hashMap:
                hashMap[ring[i]] = []
            hashMap[ring[i]].append(i)
            # count += 1

            j = -1 * i

            if ring[j] not in hashMap:
                hashMap[ring[j]] = []
            hashMap[ring[j]].append(j)
            # count += 1

        # print(hashMap)

        finalAnswer = 0

        for i in key:

            moveBy = giveAbsMin(hashMap[i])

            # update the hashMap
            for xKey in hashMap:
                for j in range(len(hashMap[xKey])):
                    hashMap[xKey][j] -= moveBy

                    if hashMap[xKey][j] > center:
                        hashMap[xKey][j] -= len(ring)
                    if hashMap[xKey][j] < -1 * center:
                        hashMap[xKey][j] += len(ring)
                # hashMap[xKey].sort()
                    # if
            if moveBy < 0:
                finalAnswer += -1 * moveBy + 1
            else:
                finalAnswer += moveBy + 1

            print(finalAnswer, "after", i, "hashMap=", hashMap, moveBy)
        return finalAnswer


        # for i in range(-1, -1*len(ring)//2 + 1)
