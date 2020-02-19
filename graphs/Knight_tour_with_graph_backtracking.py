import  my_abstract_pack.abstract_pack as ap

x_data = [-1, 1, -2, 2, -2, 2, 1, -1]
y_data = [-2, -2, -1, -1, 1, 1, 2, 2]

def build_graph_kt(n):
    graph = ap.Graphs()

    for x in range(n):
        for y in range(n):
            node_id = position_to_node(x, y, n)
            neighbor = get_neighbor_node(x, y, n)
            for move_node in neighbor:
                graph.add_edges(node_id, move_node)

    return graph

def position_to_node(x,y, board_size):
    return (x * board_size) + y

def get_neighbor_node(x, y, n):
    neightbor = []
    for i in range(8):
        new_x = x + x_data[i]
        new_y = y + y_data[i]
        if is_valid_move(new_x, new_y, n):
            neightbor.append(position_to_node(new_x, new_y, n))

    return neightbor

def is_valid_move(x, y, n):
    return -1 < x < n and -1 < y < n

def knight_tour(counter, current_node, path, gkt):
    if counter == 5 **2:
        return True

    for possible_node in current_node.get_connections():
        if possible_node.color == 'white':
            possible_node.color = 'grey'
            path.append(possible_node)

            # working as stack LIFO here as  recursion
            if knight_tour(counter+1, possible_node, path, gkt):
                return True
            else:
                # bcz of back tracking
                removed_node= path.pop()
                removed_node.color = 'white'

    return False

def knight_tour_problem(gkt):
    start = 0
    counter = 1
    path = []
    current_node = gkt.get_vertex(start)
    current_node.color = 'grey'
    path.append(current_node)
    if knight_tour(counter, current_node, path, gkt):
        print_out(path)
    else:
        print('error somthing')

def print_out(path):
    for i in path:
        print(i)

if __name__ == "__main__":
    gkt = build_graph_kt(5)
    # print (gkt)
    knight_tour_problem(gkt)