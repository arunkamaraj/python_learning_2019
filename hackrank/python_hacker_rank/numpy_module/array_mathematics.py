import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().strip().split()))
    a1 = numpy.array([list(map(int, input().strip().split())) for i in range(N)])
    a2 = numpy.array([list(map(int, input().strip().split())) for i in range(N)])

    print(a1.__add__(a2))
    print(a1.__sub__(a2))
    print(a1.__mul__(a2))
    print(a1//a2)
    print(a1.__mod__(a2))
    print(a1.__pow__(a2))



