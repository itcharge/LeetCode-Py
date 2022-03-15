class EdgeNode:                                 # 边信息类
    def __init__(self, vi, vj, val):
        self.vi = vi                            # 边的起点
        self.vj = vj                            # 边的终点
        self.val = val                          # 边的权值
        
class Graph:                                     # 基本图类，采用边集数组表示
    def __init__(self, vertices=[]):
        self.ver_count = len(vertices)          # 顶点个数
        self.vertices = vertices                # 顶点数组
        self.edges = []							# 边数组
        
    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
            
    # 向图的边数组中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        edge = EdgeNode(vi, vj, val)
        self.edges.append(edge)
        
    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        for edge in self.edges:
            if vi == edge.vi and vj == edge.vj:
                val = edge.val
                return val
        return None
    
    # 根据边数组打印图
    def printGraph(self):
        for edge in self.edges:
            print(edge.vi + ' - ' + edge.vj + ' : ' + str(edge.val))
            
vertices = ['v1', 'v2', 'v3', 'v4', 'v5']
graph = Graph(vertices)
edges = [['v1', 'v4', 3],['v1', 'v3', 9],['v3', 'v4', 6],['v2', 'v5', 4],['v4', 'v5', 2]]
graph.creatGraph(edges)
print(graph.get_edge('v3', 'v4'))
graph.printGraph()