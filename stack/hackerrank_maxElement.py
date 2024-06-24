"""
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query

Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query.

Constraints

Constraints



All queries are valid.

Sample Input

STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91

"""



#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
# time complexity O(n*n) since operation n looped n times, and max(stack) worst case is O(n), out of limits. The trick is to compare the "1" case element value, if it is smaller than the current stack top element, then reinsert the current stack top element. When "2" case, it will delete it. And "3" will always get the stack[-1] which is the maximum element, takes O(1) time.
# 
def getMax(operations):
    stack, res = [], []
    for op in operations:
        op = op.split(' ')
        if op[0] == '1':
            if stack and int(op[1]) < stack[-1]:
                stack.append(stack[-1])
            else:
                stack.append(int(op[1]))
        elif op[0] == '2' and stack:
            stack.pop()
        elif op[0] == '3':
            res.append(stack[-1])
    return res 
    # Write your code here
    # stack = []
    # res = []
    # for op in operations:
    #     op = op.split(' ')
    #     if len(op)==2 and op[0] == '1':
    #         stack.append(int(op[1]))
    #     elif op[0] == '2' and stack:
    #         stack.pop()
    #     elif op[0] == '3'and stack:
    #         print(max(stack))
    #         res.append(max(stack))
    # return res 

            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
