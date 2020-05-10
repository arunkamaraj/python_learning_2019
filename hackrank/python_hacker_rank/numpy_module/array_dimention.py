import numpy

def change_dimention(arr):
    data = numpy.array(arr, int)
    data.shape = (3, 3)
    print(data)

arr = input().strip().split(' ')
change_dimention(arr)