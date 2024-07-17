"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

 
Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

Constraints:

1 <= k <= nums.length <= 10**5
-2**31 <= nums[i] <= 2**31 - 1
"""


# brutal force

# time O(nklogk), loop through n windows, sort is klogk
# space O(k), each time create k size array
from typing import List
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         def findMedian(l, r):
#             new = sorted(nums[l:r+1])
#             # print(l, r, new)
#             if k%2 == 0: 
#                 return (new[k//2-1] + new[k//2])/2
#             if k%2: 
#                 return new[k//2]
#         n = len(nums)
#         res = []
#         for i in range(0,n-k+1):
#             l, r = i, i + k - 1
#             median = findMedian(l, r)
#             res.append(median)
#         return res


# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# # [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# print(Solution().medianSlidingWindow(nums, k))


nums = [1,2,3,4,2,3,1,4,2]
k = 3
# [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
# print(Solution().medianSlidingWindow(nums, k))


# Not quite understand why push into the min heap first, then send the first element of min heap to max heap, and check the size of max if larger than min, then max first element to min. 
# https://leetcode.com/problems/sliding-window-median/solutions/262689/python-small-large-heaps/

# balance two heaps, max heap, min heap, the size of min heap is either the same or 1 more than max heap

# [smaller half - max heap - to find max][larger half - min heap - to find min]

# algorithm


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def findMedian(l, r):
            new = sorted(nums[l:r+1])
            # print(l, r, new)
            if k%2 == 0: 
                return (new[k//2-1] + new[k//2])/2
            if k%2: 
                return new[k//2]
        n = len(nums)
        res = []
        for i in range(0,n-k+1):
            l, r = i, i + k - 1
            median = findMedian(l, r)
            res.append(median)
        return res
    

def sliding(nums, k):
    win = nums[:k]
    print(win)
    for i in range(k, len(nums)):
        win.pop(i-k)
        print(win)
        win.append(nums[i])
        print(win)
nums = [0,1,2,3,4,5]
k = 3
sliding(nums, k)

# check test.ipynb, could not figure it out. 