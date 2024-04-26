"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in place change, and also maintain the relative order of rest
        # use two pointers
        if len(nums) == 1: return nums
        l, r = 0, 1
        while r < len(nums):
            # simplified logic
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[r], nums[l] = nums[l], nums[r]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r = l+1

            # if nums[l] == 0:
            #     if nums[r] != 0:
            #         nums[l], nums[r] = nums[r], nums[l]
            #     else:
            #         while r < len(nums) - 1 and nums[r] == 0:
            #             r += 1
            #         nums[l], nums[r] = nums[r], nums[l]
            # l += 1
            # r = l + 1
                
        # use for loop seems easiler
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

        return nums
        