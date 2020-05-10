import numpy

if __name__ == "__main__":
    numpy.set_printoptions(legacy='1.13')
    data = numpy.array(list(map(float, input().strip().split())))
    print(numpy.floor(data), numpy.ceil(data), numpy.rint(data), sep='\n')

