class Solution:
    def prim(self, graph):
        size = len(graph)
        vis = set()
        dist = [float('inf') for _ in range(size)]
    
        ans = 0
        pos = 0
        dist[pos] = 0
        vis.add(pos)
    
        for i in range(1, size):
            if 0 in graph and i in graph[0]:
                dist[i] = graph[0][i]
    
        for i in range(size - 1):
            cur_min = float('inf')
            pos = -1
            for j in range(size):
                if j not in vis and dist[j] < cur_min:
                    cur_min = dist[j]
                    pos = j
            if pos == -1:
                return -1
            ans += cur_min
            vis.add(pos)
            for j in range(size):
                if j not in vis and dist[j] > graph[pos][j]:
                    dist[j] = graph[pos][j]
        return ans

points = [[0,0]]
graph = dict()
size = len(points)
for i in range(size):
    x1, y1 = points[i]
    for j in range(size):
        x2, y2 = points[j]
        dist = abs(x2 - x1) + abs(y2 - y1)
        if i not in graph:
            graph[i] = dict()
        if j not in graph:
            graph[j] = dict()
        graph[i][j] = dist
        graph[j][i] = dist
        

print(Solution().prim(graph))