# 0 ------------ 1
# |               \
# |                 \   5
# |                 /
# 3 -----------  2/
#  \         /
#   \       /           \
#    \     /            \
#       4 -----------   6

import my_abstract_pack.abstract_pack as ap

# graph_data = {0:[1,3], 1:[0,2,3,5,6], 2: [1,2,5,4], 3:[0,1,2,4], 4:[2,3,6], 5:[1,2], 6:[1,4]}

g = ap.Graphs()
dfs_path = []

# def create_graph():
#     for node in  graph_data:
#         for neighbor in  graph_data[node]:
#             g.add_edges(node, neighbor)

def create_DAG():
    g.add_edges('3/4 cup Milk', '1 cup mix')
    g.add_edges('1 egg', '1 cup mix')
    g.add_edges('1 Tbl Oil', '1 cup mix')
    g.add_edges('1 cup mix', 'heat syrup')
    g.add_edges('1 cup mix', 'pour 1/4 cup')
    g.add_edges('heat griddle', 'pour 1/4 cup')
    g.add_edges('pour 1/4 cup', 'turn when bubbly')
    g.add_edges('turn when bubbly', 'eat')
    g.add_edges('heat syrup', 'eat')

def DFS_traversal(vertex):
    vertex.color = 'grey'

    # For un directed graph
    # dfs_path.append(vertex.id)
    for depth_node in vertex.get_connections():
        if depth_node.color == 'white':
            DFS_traversal(depth_node)
        # else:
        #     pass
    node.color = 'black'
    # For DAG
    # dfs_path.insert(0, vertex.id)

if __name__ == "__main__":
    #------------------- ordinary
    # create_graph()
    # # create_DAG()
    # start = 0
    # node = g.get_vertex(0)
    # DFS_traversal(node)

    #------------------  topology
    #------------- here lot of unvisited node as it is DAG
    create_DAG()
    start = '3/4 cup Milk'
    node = g.get_vertex(start)
    DFS_traversal(node)


    # print (dfs_path)
    for i in dfs_path:
        print (i)
