import numpy

if __name__ == "__main__":
    x, y = list(map(int, input().strip().split(' ')))
    print(numpy.eye(x, y, 0))