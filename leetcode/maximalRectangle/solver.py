class Solution:
    def maximalRectangle(self, matrix):

        def findPSE(array):
            if len(array) == 0:
                return []
            if len(array) == 1:
                return [0]

            answer = [0]
            stack = [0]

            for i in range(1, len(array)):
                top = len(stack) - 1
                if array[stack[top]] < array[i]:
                    answer.append(stack[top])
                    stack.append(i)
                elif(array[stack[top]] >= array[i]):
                    while top >= 0 and array[stack[top]] >= array[i]:
                        stack.pop()
                        top = len(stack) - 1
                    stack.append(i)
                    answer.append(stack[top])
            return answer
        def findNSE(array):
            array = array[::-1]
            answer = list(map(lambda x: len(array) - x -1,findPSE(array)))
            return answer[::-1]


        countRectangle = 0


        tempArr = [0 for i in matrix[0]]
        for arr in matrix:

            for i in range(len(arr)):
                if (int(arr[i])) == 0:
                    tempArr[i] = 0
                tempArr[i] += int(arr[i])

            # print(tempArr)
            pseArr = findPSE(tempArr)
            nseArr = findNSE(tempArr)
            for i,e in enumerate(tempArr):
                # print(i,e)
                lMin = pseArr[i]
                rMin = nseArr[i]

                if lMin == i:
                    lMin = -1
                if rMin == i:
                    rMin = len(tempArr)

                tempAnswer = e * (rMin - lMin - 1)
                # print(tempAnswer, i, e)
                if tempAnswer > countRectangle:
                    countRectangle = tempAnswer

        print('answer', countRectangle)
        return countRectangle

s = Solution()
s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
