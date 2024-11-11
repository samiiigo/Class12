#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    min, max = arr, []
    for i in range(len(arr)):
        arr_=arr.copy()
        arr_.pop(i)
        
        if sum(min)>sum(arr_):
            min = arr_
        if sum(max)<sum(arr_):
            max=arr_
    
    print(sum(min), sum(max))

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
