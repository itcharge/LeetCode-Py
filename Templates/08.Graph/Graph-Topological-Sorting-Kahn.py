import collections

class solution:
    def topologicalSorting(graph):
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
        
        
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []
        
        while S:
            u = S.pop()
            order.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    S.append(v)
        
        size = len(indegrees)
        if size == len(S):
            return order
        return None