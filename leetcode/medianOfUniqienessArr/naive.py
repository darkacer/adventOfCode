class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        lenOfUniqueNessArr = (len(nums) + 1) * len(nums) // 2
        # print(lenOfUniqueNessArr)

        indexOfMedian = lenOfUniqueNessArr // 2
        # print("indexOFMEd", indexOfMedian)
        cummlativeArray = []

        for i in range(len(nums), 0, -1):
            cummlativeArray.append(i)

        # print(cummlativeArray)
        count = 0
        prevCount = 0

        lengthOfTargetSubarray = None
        for i,e in enumerate(cummlativeArray):
            prevCount = count
            count += e
            if count >= indexOfMedian:
                # print("index ", i, "value", e, "overshoot", prevCount, count)
                lengthOfTargetSubarray = i + 1
                # subArrayStartAt = e - (count - indexOfMedian) - 1
                subArrayStartAt = indexOfMedian - prevCount - 1
                break

        print(subArrayStartAt,lengthOfTargetSubarray)
        # subArray = nums[subArrayStartAt:subArrayStartAt+lengthOfTargetSubarray+1]
        subArray = []

        for i in range(subArrayStartAt, subArrayStartAt + lengthOfTargetSubarray):
            subArray.append(nums[i])

        distinct = set(subArray)
        # print(subArray)
        return len(distinct)
