import collections
INF =float('inf')
import heapq
class Dijkstra(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """


        adj ={} # 邻接表
        for i in range(1,N+1):
            adj[i] ={}



        for u, v, w in times:
            adj[u][v] =w


        def dijkstra(adj, K): #K是出发的点， 这里默认到达所有点
            arrived ={}   # 已经到的点
            pq = [(0, K)]# 存储需要到的点的最短值
            while pq:
                d, node = heapq.heappop(pq)
                if node in arrived: # 如果已经到达，
                    continue
                arrived[node] = d
                # print(node)
                for nei in adj[node]:
                    if nei not in arrived:
                        heapq.heappush(pq, (d + adj[node][nei], nei))

            return arrived


        print(dijkstra(adj, K))

Dijkstra.networkDelayTime(None,times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2)