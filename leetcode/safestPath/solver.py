# from functools import lru_cache
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution:
    def maximumSafenessFactor(self, grid):
        found = [False]
        n = len(grid)
        # tempD = [[None for j in range(n)] for i in range(n)]
        def indexToNum(i,j):
            return i * len(grid[0]) + j

        def numToIndex(num):
            return [num // len(grid[0]), num % len(grid[0])]

        def getNeighbors(i,j):
            possibles = [[-1,0],[0,-1],[1,0],[0,1]]
            neighbors = []
            for p in possibles:
                pi = i + p[0]
                pj = j + p[1]
                if pi >= 0 and pj >= 0 and pi < len(grid) and pj < len(grid) and grid[pi][pj] != 1:
                    neighbors.append([pi, pj])
            return neighbors



        def floodFill(i,j, tempD):
            # print("do floodfill here", i, j, tempD)
            if found[0]:
                return

            if i < 0 or j < 0 or i >= n or j >= n:
                return

            if tempD[i][j] == None:
                return

            if i == n - 1 and j == n - 1:
                # print("hurry!!!!")
                found[0] = True
                return

            tempD[i][j] = None

            if found[0] == False:

                floodFill(i-1,j, tempD)
                floodFill(i,j-1, tempD)
                floodFill(i+1,j, tempD)
                floodFill(i,j+1, tempD)

            return






        # write a method that uses the d matrix and solves for given num
        @lru_cache(maxsize = 128)
        def mazeRunFor(num):

            tempD = [[None for j in range(n)] for i in range(n)]
            # print("solving for", num, tempD)

            for i in range(n):
                for j in range(n):
                    if d[i][j] >= num:
                        tempD[i][j] = d[i][j]


            # print("*"*8, tempD)
            floodFill(0,0, tempD)
            if found[0] == True:
                found[0] = False
                return True
            return False








        d = [[float('inf') for _ in range(n)] for _ in range(n)]

        # print(d)

        def bfs():
            # print("doing startes", pq)
            if len(pq) == 0:
                return

            i,j = numToIndex(pq.pop(0))

            value = d[i][j]

            for p in getNeighbors(i,j):
                # p[0] and p[1]
                numVal = indexToNum(p[0],p[1])

                if numVal in pq or d[p[0]][p[1]] <= value + 1:
                    continue

                d[p[0]][p[1]] = min(d[p[0]][p[1]], value + 1)
                pq.append(numVal)
            bfs()
            # neigh = [[-1,0],[0,-1],[1,0],[0,1]]

        theifPoints = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    theifPoints.append([i,j])

        for k in theifPoints:
            i,j = k
            pq = []
            pq.append(indexToNum(i,j))
            d[i][j] = 0
            bfs()

        # print(d)


        # integer value which is at max safeness
        maxPossibleSafeness = 0
        minPossibleSafeness = float('inf')

        for i in range(n):
            for j in range(n):
                if d[i][j] > maxPossibleSafeness:
                    maxPossibleSafeness = d[i][j]
                if d[i][j] < minPossibleSafeness:
                    minPossibleSafeness = d[i][j]

        # print(maxPossibleSafeness, minPossibleSafeness)

        left = minPossibleSafeness
        right = maxPossibleSafeness

        # solvedArray = [False for i in range(right + 1)]

        if mazeRunFor(right):
            return right

        while left < right:
            mid = left + (right - left) // 2

            # if mazeRunFor(left) == False:
            #     return mid

            if mazeRunFor(mid):

                left = mid + 1
                if mazeRunFor(left) == False:
                    return mid
            else:
                right = mid - 1

        # print(left, right)
        return right


s = Solution()
print(s.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]), "*"*16)
print(s.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))
