#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_total = sum(arr)
    min_val = arr_total - max(arr)
    max_val = arr_total - min(arr)
    print(min_val, max_val)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
