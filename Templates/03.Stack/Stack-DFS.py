def dfs_recursive(graph, start, visited):
    # 标记节点
    visited.add(start)
    # 访问节点
    print(start)
    for end in graph[start]:
        if end not in visited:
            dfs_recursive(graph, end, visited)

def dfs_stack(graph, start):
    visited = set(start)
    stack = [start]

    while stack:
        node_u = stack.pop()
        # 访问节点
        print(node_u)
        for node_v in graph[node_u]:
            if node_v not in visited:
                stack.append(node_v)
                visited.add(node_v)
        

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

# 基于递归实现的深度优先搜索
visited = set()
dfs_recursive(graph, "A", visited)


# 基于堆栈实现的深度优先搜索
dfs_stack(graph, "A")
    
    