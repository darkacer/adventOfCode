class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        answer = [-1]
        shortestPathSoFarMap = {}
        pq = ['0000']

        deadends = set(deadends)



        def giveAllPossibleNeighbors(nodeString):
            neighbors = []
            # print(len(nodeString))
            for i in range(0,len(nodeString)):
                # print(i)
                tempStr = list(nodeString)
                num = int(tempStr[i])
                tempStr[i] = str((num + 1) % 10)
                neighbors.append("".join(tempStr))
                tempStr[i] = str((10 + num - 1) % 10)
                neighbors.append("".join(tempStr))

            return neighbors


        if '0000' in deadends:
            return -1

        # check if all the paths are already blocked for the target
        reqNeighbors = giveAllPossibleNeighbors(target)

        allNighborsBlocked = True
        for i in reqNeighbors:
            if i not in deadends:
                allNighborsBlocked = False
                break
        if allNighborsBlocked:
            return -1



        #######################



        def performBFS():
            if answer[0] != -1:
                return
            if len(pq) == 0:
                return


            currentNode = pq.pop(0)
            # print(shortestPathSoFarMap, "this is short")
            depth = shortestPathSoFarMap[currentNode]
            print("depth of", currentNode, "is", depth)

            if currentNode == target:
                # print("we found it at ", depth)
                answer[0] = depth
                # pq = []
                return


            # if currentNode in deadends:
            #     # print("we hit a deadend at", currentNode)
            #     return

            for i in giveAllPossibleNeighbors(currentNode):

                if i not in shortestPathSoFarMap and i not in pq and i not in deadends:
                    # print(i)
                    pq.append(i)
                    shortestPathSoFarMap[i] = depth + 1
            # print("pq len", len(pq), pq)
            performBFS()

        # pq.append('0001')
        shortestPathSoFarMap['0000'] = 0
        performBFS()
        return answer[0]
