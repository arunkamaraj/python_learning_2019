import numpy

if __name__ == "__main__":
    x,y, z = list(map(int, input().strip().split(' ')))
    print (numpy.zeros((x,y,z), int))
    print(numpy.ones((x,y,z), int))
