import numpy


if __name__ == "__main__":
    N = int(input())
    a1 = numpy.array([list(map(float, input().strip().split())) for i in range(N)])
    # print(a1)
    print(round(numpy.linalg.det(a1), 2))