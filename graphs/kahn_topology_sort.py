import my_abstract_pack.abstract_pack as ap
in_degree = {}
process_queue = []
output_list = []
counter = 0

def topology_sort():
    global counter
    while process_queue:
        item = process_queue.pop()
        # in_degree.pop(item)
        output_list.append(item)

        vertex = g.get_vertex(item)

        for adj_v in vertex.get_connections():
            in_degree[adj_v.id] -= 1

            if in_degree[adj_v.id] == 0:
                process_queue.append(adj_v.id)

        counter += 1


    if counter != g.num_vertex:
        print("error bcz it is not a DAG")
    else:
        print(output_list)


def initialize_in_degree_dict():
    for i in g.get_vertices():
        in_degree[i] = 0

def update_in_degree_and_process_q():
    for v, k in g.vertex_list.items():
        for adj_v in k.get_connections():
            in_degree[adj_v.id] += 1

    for k,v in in_degree.items():
        if v == 0:
            process_queue.append(k)
            # in_degree.pop(k)

if __name__ == "__main__":
    g = ap.Graphs() 
    g.add_edges('3/4 cup Milk', '1 cup mix')
    g.add_edges('1 egg', '1 cup mix')
    g.add_edges('1 Tbl Oil', '1 cup mix')
    g.add_edges('1 cup mix', 'heat syrup')
    g.add_edges('1 cup mix', 'pour 1/4 cup')
    g.add_edges('heat griddle', 'pour 1/4 cup')
    g.add_edges('pour 1/4 cup', 'turn when bubbly')
    g.add_edges('turn when bubbly', 'eat')
    g.add_edges('heat syrup', 'eat')

    initialize_in_degree_dict()
    print('before', in_degree)
    update_in_degree_and_process_q()
    print ('after update', in_degree)

    topology_sort()
    print ('after topology', in_degree)