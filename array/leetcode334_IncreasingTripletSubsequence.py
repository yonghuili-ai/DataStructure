"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

# setup the first two in increasing order, and then find the last number which are larger than the first two

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        first_min, second_min = float("inf"), float("inf")
        for i in range(len(nums)):
            if nums[i] <= first_min:
                first_min = nums[i]
            elif nums[i] > first_min and nums[i] <= second_min:
                second_min = nums[i]
            else:
                return True
        return False 
                

        # # failed for test cases [20,100,10,12,5,13]
        # stack = []
        # for i, v in enumerate(nums):
        #     if not stack: stack.append(v)
        #     else: 
        #         while stack and stack[-1] > v: # not align with increasing order
        #             stack.pop()
        #         # now the top in stack is smaller than v
        #         stack.append(v)
        #     # check if stack len >= 3
        #     if len(stack) >= 3:
        #         return True 
        # return False 
        
        # The stack solution will fail, but will work if the question changed to look for 3 continous incresing nums
        # class Solution:
        # def increasingTriplet(self, nums: List[int]) -> bool:
        #     stack = []
        #     for i, v in enumerate(nums):
        #         if not stack: stack.append(v)
        #         else: 
        #             while stack and stack[-1] > v: # not align with increasing order
        #                 stack.pop()
        #             # now the top in stack is smaller than v
        #             stack.append(v)
        #         # check if stack len >= 3
        #         if len(stack) >= 3:
        #             return True 
        #     return False 
        