"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    def __init__(self):
        self.cache = {} # initialize cache
    def climbStairs(self, n: int) -> int:
        # check if results are available in cache
        if n in self.cache: return self.cache[n]
        # base condition
        if n>0 and n <= 2: return n
        # recursion relation
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
        # save result to cache -- memorization
        self.cache[n]=res
        return res 
    
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
