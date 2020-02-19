import sys
class Graph:
    def __init__(self, ver_no):
        self.v_count = ver_no
        self.graph = []

    def find_path(self, cur_vertex, parent):
        if parent[cur_vertex] == - 1:
            print (cur_vertex, end='')
            return
        self.find_path(parent[cur_vertex], parent)
        print (cur_vertex, end='')

    def print_vertex_and_distance(self, distance, parent):
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(self.v_count):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" %(0, i, distance[i]), end=''), self.find_path(i, parent)

    def select_min_u_vertex(self, selected_status, min_distance):

        current_min_value = sys.maxsize
        for vertex in range(self.v_count):
            if selected_status[vertex] == False and min_distance[vertex] < current_min_value:
                current_min_value = min_distance[vertex]
                vertex_with_min_dist_index = vertex

        return vertex_with_min_dist_index

    def dijkstra(self, src):
        selected_status =[False] * self.v_count
        min_distance = [sys.maxsize] * self.v_count
        min_distance[src] = 0
        parent = [-1] * self.v_count # simple and effective

        while False in selected_status:
            # initially only src will be selected
            u_vertex = self.select_min_u_vertex(selected_status, min_distance)

            selected_status[u_vertex] = True

            for v_vertex in range(self.v_count):
                if self.graph[u_vertex][v_vertex] > 0 and selected_status[v_vertex] == False and min_distance[u_vertex] + self.graph[u_vertex][v_vertex] < min_distance[v_vertex]:
                    min_distance[v_vertex] = min_distance[u_vertex] + self.graph[u_vertex][v_vertex]
                    parent[v_vertex] = u_vertex

        self.print_vertex_and_distance(min_distance, parent)
        # print(parent)

g = Graph(9)
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

g.dijkstra(0)