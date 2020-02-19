import my_abstract_pack.abstract_pack as ap

if __name__ == "__main__":
    tree = ap.binary_tree('a')

    tree.insert_left('b')
    tree.insert_right('c')

    l = tree.get_left_child()  # spend more than 30 min
    l.insert_right('d')

    r = tree.get_right_child()
    r.insert_left('e')
    r.insert_right('f')

    print (tree)


