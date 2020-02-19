import sys
class Graph:
    def __init__(self, size):
        self.v_no = size
        self.graph =[]

    # def find_path(self):


    def find_min(self, vertex_processing_status, min_edge):
        min_cost  = sys.maxsize

        for i in range(self.v_no):
            if vertex_processing_status[i] == False and min_edge[i] < min_cost:
                min_cost = min_edge[i]
                vertex = i

        return vertex

    def prims(self):
        min_edge = [sys.maxsize] * self.v_no
        vertex_processing_status = [False] * self.v_no
        parent = [-1] * self.v_no

        # staring with 0 vertex
        min_edge[0] = 0

        while False in vertex_processing_status:
            u =  self.find_min(vertex_processing_status, min_edge)

            vertex_processing_status[u] = True

            for v in range(self.v_no):
                if g.graph[u][v] > 0 and g.graph[u][v] < min_edge[v]:
                    min_edge[v] = g.graph[u][v]
                    parent[v] = u

        print ('weight of min spanning tree is ', sum(min_edge))
        # print ('min spannig tree path', self.find_path)


if __name__ == "__main__":
    g =  Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.prims()