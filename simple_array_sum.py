import math
import os
import random
import re
import sys

def simple_array_sum(arr):
    return sum(arr)

input_string = input()
elements = list(map(int, input_string.split()))

result = simple_array_sum(elements)
print(result)
