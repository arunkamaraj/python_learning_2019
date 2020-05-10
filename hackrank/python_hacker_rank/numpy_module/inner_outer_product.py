import numpy
"""
inner product means A(T)B
outer product means AB(T)
"""
A = numpy.array(list(map(int, input().strip().split())))
B = numpy.array(list(map(int, input().strip().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))
