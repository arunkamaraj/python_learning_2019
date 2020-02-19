import my_abstract_pack.abstract_pack as ap

def pre_order(tree):
    if tree:
        print (tree.get_root_data())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())

def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.get_root_data())
        in_order(tree.get_right_child())

def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_data())

def pre_order_string(tree):
    val =" "
    if tree:
        val = tree.get_root_data()
        val = val + pre_order_string(tree.get_left_child())
        val = val + pre_order_string(tree.get_right_child())
    return  val

def in_order_string(tree):
    val =''
    if tree:
        val = in_order_string(tree.get_left_child())
        val = val + tree.get_root_data()
        val = val + in_order_string(tree.get_right_child())
    return val

def post_order_string(tree):
    val =" "
    if tree:
        val = post_order_string(tree.get_left_child())
        val = val + post_order_string(tree.get_right_child())
        val = val + tree.get_root_data()
    return  val


if __name__ == "__main__":
    expr = "( ( 4 + 3 ) * 2 )"
    tree = ap.TreeHelper.do_build_parse_tree(expr=expr)
    # print (pre_order_string(tree))
    print (post_order_string(tree))
