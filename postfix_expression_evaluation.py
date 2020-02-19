# parse the post fix notation
# push the all literals in to stack
# if ge the operator and perform on that and push the result in to stack
# do match with operands

import my_abstract_pack.abstract_pack as abstract_type
def postfix_evalution(postfixdata):
    stack = abstract_type.Stack()

    for i in postfixdata.split():
        if i in '1234567890':
            stack.push(i)
        else:
            op2= int(stack.pop())
            op1= int(stack.pop())
            result = do_math(op1, op2, i)
            stack.push(result)
        pass

    return stack.pop()


def do_math(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2


if __name__ == '__main__':
    print(postfix_evalution('7 8 + 3 2 + /'))


