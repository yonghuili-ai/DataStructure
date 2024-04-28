"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        # it is confusing if using while and defined value of right
        # in such condition, let us try with for loop on right
        # and inside for loop, use while and if
        l, res, count = 0, 0, 0 # left pointer of the sliding window, maximum length of the subarray, number of zero encountered
        for r in range(len(nums)): # sliding on the right pointer
            if nums[r] == 0:
                count += 1
            while count > 1: # max allow 1 zero
                if nums[l] == 0: # if more than 1 zero, we need to move the left pointer until passing the leftmost zero
                    count -= 1
                l += 1 # Need to move left as long as the count is bigger than 1
            res = max(res, r - l + 1 - count) # need to update the max length, remember to subtract count

        # if all are 1, then r is the same as nums lenght, then res = r + 1
        if res == len(nums):
            return len(nums) -1
        else:
            return res