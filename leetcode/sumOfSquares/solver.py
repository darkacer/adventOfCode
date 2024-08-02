MAX = 100

class Solution:

    perfectSquares = []
    findAt = 0

    priorityQueue = []
    graph = {}

    def performBFSAt(self, length):

        print('perform BFS called at', length, self.priorityQueue[0][0])

        for i in self.graph[self.priorityQueue[0][0]]:
            
            if i == self.findAt:
                # break
                return length
            self.priorityQueue.append([i,length])

        self.priorityQueue = self.priorityQueue[1:]
        length = self.performBFSAt(self.priorityQueue[0][1] + 1)
        return length



    
    def numSquares(self, n: int) -> int:

        print(n)
        self.findAt = n

        for i in range(1, MAX + 1):
            self.perfectSquares.append(i * i)

        print(self.perfectSquares)

        for i in range(n + 1):

            for j in self.perfectSquares:


                if j > i:
                    break

                print(i - j, i, j)
                # add node between i and n - i

                if (i - j) not in self.graph:
                    self.graph[i - j] = []
                (self.graph[i - j]).append(i)

        self.priorityQueue.append([0,0])
        
        answer = self.performBFSAt(0) + 1



        print(self.graph)
        return answer
    
sol = Solution()
print(sol.numSquares(7), '-'*8)
