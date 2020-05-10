def print_fun(n):
    if isinstance(n, int) and n >=1:
        for i in range(1, n+1):
            print(i, end='')

if __name__ == '__main__':
    n = int(input())
    print_fun(n)
