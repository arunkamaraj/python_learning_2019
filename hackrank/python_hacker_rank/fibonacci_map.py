def fibonacci(n):
    l = []
    a = 0
    b = 1
    for i in range(n):
        if i == 0:
            l.append(a)
        elif i == 1:
            l.append(b)
        else:
            c = a + b
            a = b
            b = c
            l.append(c)
    return l

cube = lambda x: x ** 3

if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
