"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


"""

# Define a recursive function that generates combinations.
# Specify the base case(s) to stop the recursion.
# Define the recursive step to generate combinations by considering each element either included or excluded.
# Optionally, you can add parameters to control the length of combinations, handle duplicates, or filter combinations based on certain conditions.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(cur_combination, start):
            if len(cur_combination) == k:
                res.append(cur_combination[:])
                return # base condition, exit dfs
            for i in range(start, n+1):
                cur_combination.append(i)
                dfs(cur_combination, i + 1)
                cur_combination.remove(i)
        dfs([], 1) # made change to res in dfs, need to return res directly
        return res