#!/bin/python3

# Bad Code. Follow the code from the line 57. The code starting from line 4 doesn't have improved time complexity.
# The below code from was written to understand the flow of the program.
'''import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    str1 = ''
    list2 = []
    list3 = []
    arr_copy = []
    for k in range(0, len(arr)):
        arr_copy.append(arr[k])

    arr.sort()
    last_index = int(arr[len(arr)-1][0])
    middle_index = int(len(arr_copy)/2 - 1)

    for _ in range(0, last_index + 1):
        list2.append([])

    for i in range(0, middle_index + 1):
        element_index = int(arr_copy[i][0])
        list2[element_index].append('-')

    for j in range(middle_index + 1, len(arr_copy)):
        element_index2 = int(arr_copy[j][0])
        list2[element_index2].append(arr_copy[j][1])

    for y in range(0, len(list2)):
        for z in range(0, len(list2[y])):
            list3.append(list2[y][z])

    for r in range(0, len(list3)):
        str1 = str1 + list3[r] + ' '

    print(str1)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.


def countSort(arr):
    for a in range(len(arr)//2):
        arr[a][1] = "-"
    arr.sort(key=lambda number: int(number[0]))
    for w in arr:
        print(w[1], end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
