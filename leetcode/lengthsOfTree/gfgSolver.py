class Solution:


    def sumOfDistancesInTree(self, n, edges):

        if n == 1:
            return []

        if n == 2:
            return [1,1]

        def dfs0(node, par, g, dp, size):

            size[node] = 1
            dp[node] = 0
            for nebr in g[node]:

                if(nebr != par):
                    dfs0(nebr, node, g, dp, size)
                    size[node] += size[nebr]
                    dp[node] += (dp[nebr] + size[nebr])


        def reroot(fr, to, dp, size):
            ## 'to' is no longer a child of 'from'
            dp[fr] -= size[to] + dp[to]
            size[fr] -= size[to]

            ## 'fr' is now a child of 'to'
            size[to] += size[fr]
            dp[to] += size[fr] + dp[fr]


        def dfs1(node, par, g, dp, ans, size):
            # print("node", node, ans)
            ans[node] = dp[node]
            for nebr in g[node]:
                if (par != nebr):

                    reroot(node, nebr, dp, size)


                    dfs1(nebr, node, g, dp, ans, size)

                    reroot(nebr, node, dp, size)



        def edge(a, b, g):
            ## Convert into 0-based indexing
            a -= 1
            b -= 1

            g[a].append(b)
            g[b].append(a)


        def pathSum(g, N):
            dp = [0]*N
            ans = [0]*N
            size = [0]*N


            dfs0(0, -1, g, dp, size)


            dfs1(0, -1, g, dp, ans, size)
            # print("ans", ans)
            return ans



        # edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

        N = n

        g = [0]*N
        for i in range(0, N):
            g[i] = []


        for i in edges:
            edge(i[0] + 1, i[1] + 1, g)

        # print(g)
        res = pathSum(g, N)

        # for i in range(0, N):
        #     print(res[i], end=' ')
        # print("")

        return res

s = Solution()
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(s.sumOfDistancesInTree(6, edges))
