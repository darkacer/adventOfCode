# https://leetcode.com/problems/k-th-smallest-prime-fraction/
#

class Solution:


    def kthSmallestPrimeFraction(self, arr, k: int):

        def valueAt(nums):
            # print(nums)
            return arr[nums[0]] / arr[nums[1]]

        # def heapify(maxHeap):
        #     print(maxHeap)
        #
        # def insertMaxHeap(heap, value):
        #     heap.append(value)
        #     index = len(heap) - 1
        #     while index > 0 and heap[(index - 1) // 2] > heap[index]:
        #         heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        #         index = (index - 1) // 2
        def delete_min_heap(heap):
             index = 0
             heap[index] = heap[-1]
             heap.pop()
             while True:
                 left_child = 2 * index + 1
                 right_child = 2 * index + 2
                 smallest = index
                 if left_child < len(heap) and valueAt(heap[left_child]) < valueAt(heap[smallest]):
                     smallest = left_child
                 if right_child < len(heap) and valueAt(heap[right_child]) < valueAt(heap[smallest]):
                     smallest = right_child
                 if smallest != index:
                     heap[index], heap[smallest] = heap[smallest], heap[index]
                     index = smallest
                 else:
                     break

        def insertMaxHeapArr(heap, element):
            heap.append(element)
            # print("new heap", heap)
            index = len(heap) - 1
            while index > 0 and valueAt(heap[(index - 1) // 2]) > valueAt(heap[index]):
                heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
                index = (index - 1) // 2



        n = len(arr)

        visitorCounter = 0
        # i = 0
        # j = n - 1
        # pq = [[i,j]]
        # while visitorCounter != k and len(pq) > 0:
        #     tempI = pq[0][0]
        #     tempJ = pq[0][1]
        #     if tempI + 1 < n:
        #         pq.append([tempI + 1,tempJ])
        #     if tempJ >= 1:
        #         pq.append([tempI, tempJ - 1])
        #

        # tempArr = [2,1,7,4,9]

        maxHeap = []
        # for i in tempArr:
        #     insertMaxHeap(heap, i)
        #     print(heap)
        #
        # tempArr = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]

        pq = [[0,n-1]]
        visitedMap = [[0 for i in range(n)] for j in range(n)]
        answer = []
        while visitorCounter != k and len(pq) > 0:
            # print("next best ", pq[0],  pq)
            print("next best ", pq[0], arr[pq[0][0]],"/",arr[pq[0][1]], pq)
            tempIndexes = pq[0]
            answer = pq[0]

            if tempIndexes[0] + 1 < n and visitedMap[tempIndexes[0] + 1][tempIndexes[1]] == 0:
                insertMaxHeapArr(pq, [tempIndexes[0] + 1, tempIndexes[1]])
                visitedMap[tempIndexes[0] + 1][tempIndexes[1]] = 1
            if tempIndexes[1] - 1 >= 0 and visitedMap[tempIndexes[0]][tempIndexes[1] - 1] == 0:
                insertMaxHeapArr(pq, [tempIndexes[0], tempIndexes[1] - 1])
                visitedMap[tempIndexes[0]][tempIndexes[1] - 1] = 1
            delete_min_heap(pq)
            # print("afyer", pq)
            visitorCounter += 1
            visitedMap[tempIndexes[0]][tempIndexes[1]] = visitorCounter

        # for i in tempArr:
        #     insertMaxHeapArr(maxHeap, i)
        #     print(maxHeap)
        # delete_min_heap(maxHeap)
        # delete_min_heap(maxHeap)
        # print("after delete", maxHeap)
        # for i in maxHeap:
        #     print(arr[i[0]], "/", arr[i[1]], end=" , ")
        # print("")
        #
        return answer










s = Solution()
s.kthSmallestPrimeFraction([1,2,3,25], 11)
