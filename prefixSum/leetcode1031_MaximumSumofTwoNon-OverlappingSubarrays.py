"""
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.
 

Constraints:

1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        if firstLen + secondLen > n: return 0
        p = [0 for _ in range(n+1)]
        for i,v in enumerate(nums):
            p[i+1] = p[i] + v



    #     [0,6,5,2,2,5,1,9,4]
    # prefixSum p
    #   [0,0,6,11,13,15,20,21,30,34]
    #    0,1,2, 3, 4, 5, 6, 7, 8, 9
    #    P[L] = p[i-M] - p[i-L-M] = p[3-2] - p[3-1-2] = p[1] - p[0] = 0
    #    p[i]-p[i-M] = p[3] - p[1] = 11
    #    P[L] = p[i-M] - p[i-L-M] = p[4-2] - p[4-1-2] = p[2] - p[1] = 6
    #    p[i]-p[i-M] = p[4] - p[2] = 13 - 6 = 7
    #    P[L] = p[i-M] - p[i-L-M] = p[5-2] - p[5-1-2] = p[3] - p[2] = 5
    #    p[i]-p[i-M] = p[5] - p[3] = 15 - 11 = 4
    #    p[L] = p[i-M] - p[i-L-M] = p[6-2] - p[6-1-2] = p[4] - p[3] = 2
    #    P[L] = p[i-M] - p[i-L-M] = p[7-2] - p[7-1-2] = p[5] - p[4] = 2

    # 1. Scan the prefix sum array from index L + M, which is the first possible position;
    # 2. update the max value of the L-length subarray; then update max value of the sum of the both;
    # 3. we need to swap L and M to scan twice, since either subarray can occur before the other.
    # 4. In private method, prefix sum difference p[i - M] - p[i - M - L] is L-length subarray from index i - M - L to i - M - 1, and p[i] - p[i - M] is M-length subarray from index i - M to i - 1.
            # https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/solutions/279221/java-python-3-two-easy-dp-codes-w-comment-time-o-n-no-change-of-input/
        def maxSum(L,M):
            maxL, ans = 0, 0
            for i in range(L+M, len(p)):
                maxL = max(maxL, p[i-M] - p[i-M-L]) # see graph in the above link
                ans = max(ans, maxL + p[i] - p[i-M]) # secure maxL for L,M case, then secure maxM when call function maxSum(M,L)
            return ans
        return max(maxSum(firstLen,secondLen), maxSum(secondLen, firstLen))
    
# O(N) time
# O(N) space prefix array

        