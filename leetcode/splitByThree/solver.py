# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-01-31

class Solution:
    def divideArray(self, nums, k):
        max = 0
        for i in nums:
            if i > max:
                max = i

        countArray = [0 for x in range(max + 1)]

        for i in nums:
            countArray[i] += 1

        answerArray = []

        tempPointer = 0
        tempArray = []

        while tempPointer < len(countArray):
            if len(tempArray) < 3 and countArray[tempPointer] != 0:
                countArray[tempPointer] -= 1
                tempArray.append(tempPointer)

            if len(tempArray) == 3:
                # check if the formed array agrees to the conditions 
                if (
                    (abs(tempArray[0] - tempArray[1])) <= k
                    and abs(tempArray[1] - tempArray[2]) <= k
                    and abs(tempArray[0] - tempArray[2]) <= k
                ):
                    answerArray.append(tempArray)
                    tempArray = []
                else:
                    # print('violates conditon')
                    return []
            
            if countArray[tempPointer] == 0:
                tempPointer += 1

        print(answerArray)
        return answerArray
        

Solution().divideArray([1,3,4,8,7,9,3,5,1], 2)
Solution().divideArray([82,139,107], 186)


