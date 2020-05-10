#!/bin/python3

import math
import os
import random
import re
import sys

valid_pattern = "[a-zA-Z0-9!@#$%& ]*"
find_spl_chr = "(?<=[A-Za-z0-9])[!@#$%& ]+(?=[A-Za-z0-9])"

def column(matrix, i):
    return [row[i] for row in matrix]

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input().strip()
    matrix.append(matrix_item)

final_data = ''.join([''.join(column(matrix, j)) for j in range(len(matrix[0]))])

print(re.sub(find_spl_chr, ' ', final_data))



