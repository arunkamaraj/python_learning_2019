import numpy


def do_tarspose_flattern(arr):
    print(arr.transpose(), arr.flatten(), sep='\n')


if __name__ == "__main__":
    """
    You are given a NXM integer array matrix with space separated elements ( N= rows and  M= columns).
    Your task is to print the transpose and flatten results.
    """
    N, M = list(map(int, input().strip().split()))
    do_tarspose_flattern(numpy.array([list(map(int, input().strip().split())) for _ in range(N)]))
