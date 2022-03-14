def creatGraph(ver_count, edges=[]):
    adj_matrix = [[None for _ in range(ver_count)] for _ in range(ver_count)]
    
    for start, end, weight in edges:
        adj_matrix[start][end] = weight
        adj_matrix[end][start] = weight # 无向图
        
    for row in range(ver_count):
        for col in range(ver_count):
            if adj_matrix[row][col]:
                print(row, ' - ', col)
            
edges = [[1, 4, 3],[1, 3, 9],[3, 4, 6],[2, 5, 4],[4, 5, 2]]
creatGraph(6, edges)