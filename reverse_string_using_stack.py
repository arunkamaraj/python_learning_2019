import sys
import  my_abstract_pack.abstract_pack as abstarct_type



def do_string_reverse(data):
    stack = abstarct_type.Stack()

    reversed_string = ''

    for ch in data:
        stack.push(ch)

    while 0 < stack.size():
        reversed_data = stack.pop()
        reversed_string = reversed_string + reversed_data

    return reversed_string

if  __name__ ==  '__main__':
    mydata = sys.argv[1]
    print (do_string_reverse(mydata))