#  define the post fix result list
#  cerate stack for operator
#  define operator priority dict
#  parse infix string
# if "ABCD...."
#     append.result()
# elif ( push
# elif )
#     s = s.pop()
#     while s != '('
#         resilt.append(s)
#         s = s.pop()
# else:
#     if s.is_empty()
#         s.push()
#     else:
#         priority[s.peak] > priority[sting]
#             p = s.pop()
#             append.result()
#             s.push(string)
#         else
#             s.push()

import my_abstract_pack.abstract_pack as abtract_type
def infix_to_postfix(infix_data):
    postfix_list = []
    stack = abtract_type.Stack()
    priority ={
        '(':1,
        '+':2,
        '-':2,
        '*':3,
        '/':3,
        '**':4
    }
    for i in infix_data.split( ):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '1234567890':
            postfix_list.append(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            data = stack.pop()
            while data != '(':
                postfix_list.append(data)
                data = stack.pop()
        else:
            if stack.is_empty():
                stack.push(i)
            else:
                if priority[stack.peek()] > priority[i]:
                    postfix_list.append(stack.pop())
                stack.push(i)

    while not stack.is_empty():
        postfix_list.append(stack.pop())

    return ''.join(postfix_list)


if __name__== '__main__':
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


