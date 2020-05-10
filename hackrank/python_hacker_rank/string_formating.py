def print_formatted(number):
    width = len("{:b}".format(number))
    for i in range(1, number+1):
        print("{0:>{1}} {0:>{1}o} {0:>{1}X} {0:>{1}b}".format(i, width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)