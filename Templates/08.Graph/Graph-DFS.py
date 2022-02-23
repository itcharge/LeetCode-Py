def dfs_recursive(graph, start, visited):
    # 标记节点
    visited.add(start)
    # 访问节点
    print(start)
    for end in graph[start]:
        if end not in visited:
            dfs_recursive(graph, end, visited)

def dfs_stack(graph, start):
    print(start)                        # 访问节点 start
    visited = set(start)                # 使用 visited 标记访问过的节点，先标记 start
    stack = [start]                     # 创建一个栈，并将 start 加入栈中
    
    while stack:
        node_u = stack[-1]              # 取栈顶元素
        
        i = 0
        while i < len(graph[node_u]):   # 遍历栈顶元素，遇到未访问节点，访问节点并跳出。
            node_v = graph[node_u][i]
            
            if node_v not in visited:   # node_v 未访问过
                print(node_v)           # 访问节点 node_v
                stack.append(node_v)    # 将 node_v 加入栈中
                visited.add(node_v)     # 标记为访问过 node_v
                break
            i += 1
        
        if i == len(graph[node_u ]):    # node_u 相邻的节点都访问结束了，弹出 node_u
            stack.pop()

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
    
    