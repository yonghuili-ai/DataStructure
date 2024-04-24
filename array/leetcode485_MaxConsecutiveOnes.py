"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""




class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        num = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                num += 1
                count = max(num, count)
            else:
                num = 0
            i += 1
        return count






