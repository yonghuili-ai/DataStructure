"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 10**4
-1000 <= nums[i] <= 1000
-107 <= k <= 10**7

"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # use cumulative sum 
        # create a new sum list, index 0 value is 0, and index i value is sum(nums[0:i])
        # nums = [a0, a1, a2, a3, ... a(n-1)]
        # prefix_sum = [0, a0, a0+a1, a0+a1+a2, ....]
        # prefix_sum[right] - prefix[left] = sum(nums[left:right])
        # for example [1,2,3] ==> [0, 1, 3, 6] prefix_sum[3] - prefix_sum[1] = a1+a2 = sum(nums[1:3])

        sum_num = [0 for _ in range(len(nums)+1)]
        count = 0
        for i in range(1, len(nums)+1):
            sum_num[i] = sum_num[i-1] + nums[i-1] # construct prefix sum array
        for right in range(1, len(nums)+1):
            for left in range(right):
                if k == sum_num[right] - sum_num[left]:
                    count += 1
        return count 
# time O(n**2) when nums at 10**4 scale, need to use time complex at nlogn or lower
    # https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4725/
# spacke O(n)


import collections  
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = collections.defaultdict(int)
        res = 0
        curr_sum = 0
        # for prefix sum issue, 0 has a natural 1 time occrance
        prefix_sums[0] = 1
        # The idea behind this approach is: if the cumulative sum (represented by sum[i] for sum up to ith index) for two different indeces is the same, the sum of the elements lying in between those two indices is zero. Further more, if the cumulative sum up to two indices, i and j has: sum[i] - sum[j] = k, mean the sum of elements lying between indices i and j is k.
        # we can use a hashmap to store the cumulative sum for all the indices along with the number of times the same sum occurs, in the form of (sum_i, num of occurrence of sum_i). We traverse over the array nums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponsing to that sum. 
        # For every sum encountered, we also check if sum - k already occurred, if found, then needs to add the occurance to the final result. 
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum - k in prefix_sums:
                res += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1
        return res

        



        