import my_abstract_pack.abstract_pack as ap



# A recursive function used by topologicalSort
def topologicalSortUtil(v,stack):

    # Mark the current node as visited.
    v.color = 'grey'

    # actual DFS
    # stack.append(v.id)

    # Recur for all the vertices adjacent to this vertex
    for i in v.get_connections():
        if i.color == 'white':
            topologicalSortUtil(i,stack)

    # Push current vertex to stack which stores result
    stack.insert(0,v.id)

# The function to do Topological Sort. It uses recursive
# topologicalSortUtil()
def topologicalSort():
    # Mark all the vertices as not visited
    stack =[]

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in ['eat','3/4 cup Milk', '1 egg', '1 Tbl Oil','1 cup mix', 'pour 1/4 cup', 'heat griddle','turn when bubbly', 'heat syrup']:
        v = g.get_vertex(i)
        if v.color == 'white':
            topologicalSortUtil(v,stack)

    # Print contents of stack
    print (stack)


if __name__ == "__main__":
    g= ap.Graphs()
    g.add_edges('3/4 cup Milk', '1 cup mix')
    g.add_edges('1 egg', '1 cup mix')
    g.add_edges('1 Tbl Oil', '1 cup mix')
    g.add_edges('1 cup mix', 'heat syrup')
    g.add_edges('1 cup mix', 'pour 1/4 cup')
    g.add_edges('heat griddle', 'pour 1/4 cup')
    g.add_edges('pour 1/4 cup', 'turn when bubbly')
    g.add_edges('turn when bubbly', 'eat')
    g.add_edges('heat syrup', 'eat')

    print ("Following is a Topological Sort of the given graph")
    topologicalSort()
