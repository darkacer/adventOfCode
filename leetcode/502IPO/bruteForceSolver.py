class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        def indexOfMaxNum(arr):
            index = 0
            for i in range(len(arr)):
                if arr[i] > arr[index]:
                    index = i

            return index

        while k > 0:

            eligibleArr = [profits[i] for i in range(n) if capital[i] <= w]

            print(eligibleArr)
            index = indexOfMaxNum(eligibleArr)
            print(index)
            w += profits[index]

            profits[index] = 0

            print("new w", w)
            k -= 1

        # eligibleArr = [profits[i] for i in range(n) if capital[i] <= w]

        # print(eligibleArr)
        # print(indexOfMaxNum(eligibleArr))


        return w
