"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

"""
# Use sliding window to initial the window from the first k elements
# then move i from 1 to then end, which is n-k (in range, needs to use n-k+1)
# then the time complex is O(n)
# spack O(1)
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # O(n), O(1)
        n = len(nums)
        if n == 1 and k ==1: return round(nums[0],5)
        k_sum = 0
        res = -float("inf")
        # initial sliding window
        for j in range(k):
            k_sum += nums[j]
        res = max(res, k_sum)
        for i in range(1, n-k+1):
            k_sum = k_sum - nums[i-1] + nums[i+k-1]
            res = max(res, k_sum)
        return  round(res/k, 5)