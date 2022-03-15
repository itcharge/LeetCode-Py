class Graph:                                    # 基本图类，采用邻接矩阵表示
    # 图的初始化操作，vertices 为顶点
    def __init__(self, vertices=[]):
        self.ver_count = len(vertices)          # 顶点个数
        self.vertices = vertices                # 顶点数组
        self.adj_matrix = [[None for _ in range(self.ver_count)] for _ in range(self.ver_count)]  # 邻接矩阵
    
    # 判断顶点 v 是否有效
    def __valid(self, v):
        if v in self.vertices:
            return True
        return False
    
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
    
    # 向图的邻接矩阵中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        
        vi_index = self.vertices.index(vi)
        vj_index = self.vertices.index(vj)
        self.adj_matrix[vi_index][vj_index] = val
    
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        
        vi_index = self.vertices.index(vi)
        vj_index = self.vertices.index(vj)
        return self.adj_matrix[vi_index][vj_index]
    
    # 根据邻接矩阵打印图的边
    def printGraph(self):
        for vi in self.vertices:
            for vj in self.vertices:
                val = self.get_edge(vi, vj)
                if val:
                    print(vi + ' - ' + vj + ' : ' + str(val))
    
vertices = ['v1', 'v2', 'v3', 'v4', 'v5']
graph = Graph(vertices)
edges = [['v1', 'v4', 3],['v1', 'v3', 9],['v3', 'v4', 6],['v2', 'v5', 4],['v4', 'v5', 2]]
graph.creatGraph(edges)
graph.printGraph()