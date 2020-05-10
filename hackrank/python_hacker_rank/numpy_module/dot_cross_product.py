import numpy

if __name__ =="__main__":
    N= int(input())
    A = numpy.array([list(map(int, input().strip().split())) for i in range(N)])
    B = numpy.array([list(map(int, input().strip().split())) for i in range(N)])

    dot_output= numpy.dot(A, B)
    # cross_output = numpy.cross(A,B)
    print(dot_output)
    # print(cross_output)


# sample input
# 2 - N integer
# 1 2 -A array
# 3 4 -A
# 1 2 -B
# 3 4 -B array