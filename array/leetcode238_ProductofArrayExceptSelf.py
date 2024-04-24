"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
# O(N), O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need to remember the trick 
        # we can use the product of all the numbers to the left, and all the numbers to the right of the index
        # multiplying these two individual productions give us teh desired result
        n = len(nums)
        res = []
        if n == 1: return [1]
        L = [1 for _ in range(n)] # L[i] contains the product of all the numbers to the left of i
        R = [1 for _ in range(n)] # R[i] contains the product of all the numbers to the right of i 
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            R[j] = R[j+1] * nums[j+1]
        for i in range(n):
            res.append(L[i] * R[i])
        return res


# O(N), O(1)
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need to remember the trick 
        # we can use the product of all the numbers to the left, and all the numbers to the right of the index
        # multiplying these two individual productions give us teh desired result
        n = len(nums)
        res = [0 for _ in range(n)]
        if n == 1: return [1]
        L = [1 for _ in range(n)] # L[i] contains the product of all the numbers to the left of i
        R = 1 
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for j in reversed(range(n)):
            res[j] = R * L[j]
            R *= nums[j]

        return res


