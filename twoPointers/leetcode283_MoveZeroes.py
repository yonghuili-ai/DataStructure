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

1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

# best logic to use in interview
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in place change, and also maintain the relative order of rest
        # use two pointers
        if len(nums) == 1: return nums
        l, r = 0, 1 # also works with l, r = 0, 0
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
        
# solution that works best for interview

# if no order of non-zero elements is required. and return the count of non-zero elements.
def swap(nums): # two ends pointers
    # edge
    if len(nums) == 1 and nums[0] != 0: return 1
    if len(nums) == 1 and nums[0] == 0: return 0
    if not nums: return 0

    l, r = 0, len(nums)-1 # 0, 6
    res = 0
    while l < r:
        if nums[l] != 0 and nums[r] == 0:
            # pass wrong condition, infinite loop
            l += 1
            r -= 1
        elif nums[l] == 0 and nums[r] != 0:
            # swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] == 0 and nums[r] == 0:
            r -= 1
        elif nums[l] != 0 and nums[r] != 0:
            l += 1
    # return l wrong terminate solution
    for i in range(len(nums)):
         if nums[i] != 0:
              res += 1
    return res 


# if order of non-zero elements is required. and return the count of non-zero elements.
# two pointers from the same end
# fast or current pointer to iterate over the array
# slow or first_zero pointer track the first zero position which will be used for swap

def swap(nums):
    # first_zero = 0
    slow = 0
    # for curr in range(len(nums)):
    # if nums[curr] != 0:
    #     nums[curr], nums[first_zero] = nums[first_zero], nums[curr]
    #     first_zero += 1
    for fast in range(len(nums)): # as long as the current is nonzero, we can swap
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
        
        # elif nums[curr] != 0:
        #     first_zero = curr
        # elif nums[first_zero] == 0:
        #     first_zero += 1
    print(nums)
    return  slow #first_zero
