import my_abstract_pack.abstract_pack as ap

if __name__ == "__main__":
    # tree = ap.binary_tree_list_rep(3)
    # root = tree.t
    # tree.insert_left(root,4)
    # tree.insert_left(root,5)
    # tree.insert_right(root,6)
    # tree.insert_right(root,7)
    #
    # print (tree.get_left())
    # print (tree.t)

    x = ap.binary_tree_list_rep('a')
    root = x.t
    x.insert_left(root,'b')
    x.insert_right(root,'c')
    x.insert_right(x.get_right(root),'d')
    x.insert_left(x.get_right(x.get_right(root)),'e')

    print (root)