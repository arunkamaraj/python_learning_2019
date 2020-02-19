import my_abstract_pack.abstract_pack as abstrct_type

def convert_from_decimal(decimal_data, base):

    format ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    converetd_result = ''

    stack = abstrct_type.Stack()
    while 0 < decimal_data:
        rem = decimal_data % base
        stack.push(rem)
        decimal_data //= base

    while not stack.is_empty():
        res = stack.pop()
        # print (str(res))
        converetd_result += format[res]

    return converetd_result

if __name__ == '__main__':
    print (convert_from_decimal(10, base=16))
