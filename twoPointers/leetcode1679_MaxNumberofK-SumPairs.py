"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 
"""

# Brutal force, out of time complex

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         # brutal force
#         # for each index in nums, find all possible solutions, then find the max combination
#         res = 0
#         i = 0
#         visited = set()
#         while i < len(nums):
#             j = i + 1
#             while j < len(nums):
#                 if nums[i] + nums[j] == k and i not in visited and j not in visited:
#                     visited.add(i)
#                     visited.add(j)
#                     res += 1
#                     # print(i,j)
#                 j += 1
#             i += 1
#         return res
        
# Approach 2: Using Hashmap - Two Pass O(n), O(1)
from collections import defaultdict
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        h = defaultdict(int)
        print(h)
        res = 0
        for x in nums:
            h[x] += 1
        print(h)
        for x in nums:
            if k-x in h:
                h[k-x] -= 1
                h[x] -= 1
                if h[x] >= 0 and h[k-x] >= 0:
                    res += 1
        return res
        