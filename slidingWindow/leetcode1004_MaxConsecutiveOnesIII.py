"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 10**5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
# https://leetcode.com/problems/max-consecutive-ones-iii/
from collections import defaultdict
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """typical problem that can be solved using sliding window and hashmap
        only move right or left pointer at a time, use hashmap to save count of 0 and 1
        if moving right cause count of 0 in hashmap larger than k, means we need to move left pointer towards right
        when moving left pointer, we need to update the hashmap count, and check if count of 0 equals to k
        then record the current window to max_v"""
        l, r, max_v = 0, 0, 0
        h = defaultdict(int)
        for r, v in enumerate(nums):
            h[v] += 1
            while h[0] > k:
                # move left pointer, and update the count brought by left change in hashmap
                h[nums[l]] -= 1
                l += 1

            # if h[0] == k: max_v = max(max_v, r-l+1) # miss the case that [0,0,0,1] k = 4, should return 4, but this will return 0 
            # check all possible solutions
            max_v = max(max_v, r - l + 1)
        return max_v