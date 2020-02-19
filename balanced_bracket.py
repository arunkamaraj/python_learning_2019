import my_abstract_pack.abstract_pack as abstarct_type

def balance_check(data):
    stack = abstarct_type.Stack()
    is_balanced = True
    i = 0
    start = "{(["
    end = "})]"


    def is_match(pop_data, data):
        return start.index(pop_data) == end.index(data)

    while  is_balanced and i < len(data):
        if  data[i] in start:
            stack.push(data[i])
        else:
            # important
            if stack.is_empty():
                is_balanced = False
            else:
                pop_data = stack.pop()
                if not is_match(pop_data, data[i]):
                    is_balanced = False
        i += 1

    return is_balanced and stack.is_empty()

if __name__ == '__main__':
    print (balance_check('{({[]})}'))

    print (balance_check('{{{{}}})({}]]('))

    print (balance_check('}'))

    #define the use case to have return is_balanced and stack.is_empty()
    print (balance_check('{()'))
