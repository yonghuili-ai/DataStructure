# use memorization on dfs
# cache already known result, essentially is a dictionary
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

class Solution:
    def __init__(self):
        self.cache = {}
    def fib(self, n):
        # check if argment is already in cache
        if n in self.cache: return self.cache[n]

        # base case
        if n < 2: return n 
        # recursion relation 
        else: # or if n >= 2: much faster on time
            res = self.fib(n-1) + self.fib(n-2)
        
        # memorize the answer
        self.cache[n] = res 
        return res 

print(Solution().fib(5))
print(Solution().fib(2))