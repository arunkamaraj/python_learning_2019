import numpy

# axis is important
if __name__ == "__main__":
    N, M, P = list(map(int, input().strip().split(' ')))
    N_P_array = numpy.array([list(map(int, input().strip().split(' '))) for i in range(N)])
    M_P_array = numpy.array([list(map(int, input().strip().split(' '))) for i in range(M)])
    print (numpy.concatenate((N_P_array, M_P_array), axis=0))


