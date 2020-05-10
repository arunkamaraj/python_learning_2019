import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    data = []
    for i in range(4):
        for j in range(4):
            partial = []
            for m in range(i, i+3):
                for n in range(j,j+3):
                    if m == i+1 and (n == j or n == j + 2):
                        continue
                    partial.append(arr[m][n])
            data.append(sum(partial))
    print(max(data))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # arr = []
    #
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [ [1,1,1,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,0,2,4,4,0],
            [0,0,0,2,0,0],
            [0,0,1,2,4,0]]

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
