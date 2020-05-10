import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().strip().split()))
    a = numpy.array([list(map(int, input().strip().split())) for i in range(N)])
    min_data = numpy.min(a, axis=1)
    max_data = numpy.max(min_data)
    print(max_data)