import numpy
if __name__ == "__main__":
    ploy = list(map(float, input().strip().split()))
    x = float(input())
    print(numpy.polyval(ploy, x))
    # numpy.polyval([1, -2, 0, 2], 4)