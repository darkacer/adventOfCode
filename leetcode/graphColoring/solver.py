class Graph:

    nodesInGraph = {}
    colorsOfGraph = {}
    visited = []

    def __init__(self):
        self.nodesInGraph = {}
        self.colorsOfGraph = {}
        self.visited = []

    def addEdge(self,node1,node2):
        if node1 not in self.nodesInGraph:
            self.nodesInGraph[node1] = []
        self.nodesInGraph[node1].append(node2)
        
        if node2 not in self.nodesInGraph:
            self.nodesInGraph[node2] = []
        self.nodesInGraph[node2].append(node1)

    def colorTheGraph(self):
        counter = 0

        def bfs(currentNode):
            if currentNode in self.visited:
                return 
            neighbors = self.nodesInGraph[currentNode]
            self.visited.append(currentNode)

            for n in neighbors:
                self.colorsOfGraph[n] = self.colorsOfGraph[currentNode]
                if n not in self.visited:
                    bfs(n)
            return
        
        for n in list(self.nodesInGraph.keys()):
            if n not in self.visited:
                self.colorsOfGraph[n] = counter
                bfs(n)
                counter += 1
        # print(self.colorsOfGraph)
        # return self.colorTheGraph

        colorsMap = {}

        for i in self.colorsOfGraph:

            if self.colorsOfGraph[i] not in colorsMap:
                colorsMap[self.colorsOfGraph[i]] = []
            colorsMap[self.colorsOfGraph[i]].append(i)

        print(colorsMap)
        return colorsMap


class Solution:
    def findAllPeople(self, n, meetings, firstPerson):

        knowsSecret = [0 for i in range(0,n)]
        knowsSecret[firstPerson] = 1
        knowsSecret[0] = 1
        print(knowsSecret, '@'*8)

        meetingsByTimeLine = {}

        for i in meetings:
            # print(i[2])

            if i[2] not in meetingsByTimeLine:
                meetingsByTimeLine[i[2]] = []
            (meetingsByTimeLine[i[2]]).append([i[0], i[1]])

        print(meetingsByTimeLine, '$$$$$$')

        for time in range(0, max(meetingsByTimeLine.keys()) + 1):

            
            if time in meetingsByTimeLine:
                g = Graph()
                for meet in meetingsByTimeLine[time]:

                    personA = meet[0]
                    personB = meet[1]
                    # create a graph
                    g.addEdge(personA,personB)
                mapOfColors = g.colorTheGraph()

                for room in mapOfColors:
                    print(room)

                    someOneKnowsSecret = False
                    for person in mapOfColors[room]:
                        if knowsSecret[person] == 1:
                            someOneKnowsSecret = True
                            break
                        
                    if someOneKnowsSecret:

                        for person in mapOfColors[room]:
                            knowsSecret[person] = 1


        # print(meetingAttended)

        finalAnswer = []
        for i in range(len(knowsSecret)):
            if knowsSecret[i] == 1:
                finalAnswer.append(i)
        return finalAnswer
        

s = Solution()
# print(s.findAllPeople(5, [[1,4,3],[0,4,3]], 3), 'final answer')
# print(s.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1), 'final answer')
# print(s.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3), 'final answer')
print(s.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3), 'final answer')
# s.findAllPeople(6, [[0,2,1],[1,3,1],[4,5,1]], 1)