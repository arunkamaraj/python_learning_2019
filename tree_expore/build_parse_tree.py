import my_abstract_pack.abstract_pack as ap
import operator

operator_dict ={
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def do_build_parse_tree(expr):
    token_list = expr.split()
    bt = ap.binary_tree('')
    stack = ap.Stack()
    stack.push(bt)# to avoid ) final closing bracket we are hitting null index so
    current_node = bt

    for i in token_list:
        if i == '(':
            current_node.insert_left('')
            stack.push(current_node)
            current_node = current_node.get_left_child()

        elif i in [str(j) for j in range(100)]:
            current_node.set_root_data(i)
            current_node = stack.pop()

        elif i in ['+', '-', '*', '/']:
            current_node.set_root_data(i)
            stack.push(current_node)
            current_node.insert_right('')
            current_node = current_node.get_right_child()
        elif i == ')':
            current_node = stack.pop()
            # stack.push(current_node)
        else:
            print ('unknown tokens', i)

    return bt

def parse_tree_evaluator(pt): # this is post order traversal
    left = pt.get_left_child()
    right = pt.get_right_child()
    # print(pt.get_root_data())


    if left and right:
        # print(pt.get_root_data())
        fun = operator_dict[pt.get_root_data()]
        data = fun(parse_tree_evaluator(left),parse_tree_evaluator(right))
    else:
        return int(pt.get_root_data())

    return data


if __name__ == "__main__":
    pt = do_build_parse_tree("( ( 10 + 5 ) + 3 )")
    # print (pt.get_root_data())
    print(parse_tree_evaluator(pt))
    # pt.postorder()  # defined and explained in the next section


