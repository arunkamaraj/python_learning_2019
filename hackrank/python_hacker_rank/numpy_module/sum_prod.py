import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().strip().split()))
    a = numpy.array([list(map(int, input().strip().split())) for i in range(N)])
    sum_data = numpy.sum(a, axis=0)
    prod_data = numpy.prod(sum_data)
    print(prod_data)