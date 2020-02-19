from my_abstract_pack.abstract_pack import Graphs

if __name__ == "__main__":
    g_obj = Graphs()
    g_obj.add_both_edges('sam', 'marry')
    g_obj.add_both_edges('marry', 'joe')
    g_obj.add_both_edges('joe', 'tom')
    g_obj.add_both_edges('marry', 'tom')
    g_obj.add_vertex('sally')

    # print (g_obj.get_vertices())

    for each in g_obj.get_vertices():
        print (g_obj.vertex_list[each])
