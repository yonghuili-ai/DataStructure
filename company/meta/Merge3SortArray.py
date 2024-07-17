"""
Question 2: Merge 3 Sorted Arrays and the output array should not have any duplicates. Solve it in linear time.
https://leetcode.com/discuss/interview-question/542586/facebook-phone-merge-3-sorted-arrays
[[1,4,5],[1,3,4],[2,6]]
"""
# Question 1: https://leetcode.com/problems/merge-sorted-array/description/
# question 3: https://leetcode.com/problems/merge-k-sorted-lists/description/

"""Question 1:"""
# input: 
# num1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n=3

# def merge_2_arr(num1, num2, m, n): # O(nlogn)
#     num1[m:] = num2
#     num1.sort()
#     return num1
# print(merge_2_arr([1,2,3,0,0,0],[2,5,6], 3, 3))

num1 = [1,2]
# [1,2,3]
num2 = [2,5,6,7]
def merge_2_arr_kn(num1, num2): # O(kn) k is the number of array, O(n) need res
    i = j = 0
    m, n = len(num1), len(num2)
    res = []
    while i < m and j < n:
        if num1[i] >= num2[j]:
            res.append(num2[j])
            j += 1
        else:
            res.append(num1[i])
            i += 1
    if i == m:
        res.extend(num2[j:])
    if j == n:
        res.extend(num1[i:])
    return res

# print(merge_2_arr_kn(num1, num2))


nums = [[1,4,5],[1,3,4],[2,6]]
def merge_3_arr(nums): # sort O(nlogn)
    res = []
    for l in nums:
        res.extend(l)
    return sorted(res)

# print(merge_3_arr(nums))

def merge_3_arr_kn(nums): # O(kn), space O(n)
    i = j = k = 0
    res = []
    len1, len2, len3 = len(nums[0]), len(nums[1]), len(nums[2])
    while i < len1 and j < len2 and k < len3:
        min3 = min(nums[0][i], nums[1][j], nums[2][k])
        res.append(min3)
        if min3 == nums[0][i]: i += 1
        elif min3 == nums[1][j]: j += 1
        else: k += 1
    # print(res)
    
    def merge_2_arr(num1, num2): # O(kn) k is the number of array, O(n) need res
        i = j = 0
        m, n = len(num1), len(num2)
        res = []
        while i < m and j < n:
            if num1[i] >= num2[j]:
                res.append(num2[j])
                j += 1
            else:
                res.append(num1[i])
                i += 1
        if i == m:
            res.extend(num2[j:])
        if j == n:
            res.extend(num1[i:])
        return res
    
    if i == len1:
        rest = merge_2_arr(nums[1][j:], nums[2][k:])
    elif j == len2: 
        rest = merge_2_arr(nums[0][i:], nums[2][k:])
    elif k == len3:
        rest = merge_2_arr(nums[0][i:], nums[1][j:])
    res.extend(rest)
    return res
# print(merge_3_arr_kn(nums))

from heapq import *
def merge_3_arr_n(nums): # O(nlogk) time, n is the total element in nums, k is average length of each list in nums
    # space O(n) since needs n size list for heap
    heap = []
    res = []
    for num in nums: # Run n times heappush, n is the total element in nums
        for i in range(len(num)):
            heappush(heap, num[i]) # O(logk) for heappush, and k is the size of the array
    # print(heap)
    while heap: 
        curr = heappop(heap) # O(1) for heappop, loop the whole heap is O(n)
        res.append(curr)
    print(res)
merge_3_arr_n(nums)

# 23. Merge k Sorted Lists???
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10**4
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 10**4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10**4.
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        # create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy

        while min_heap:
            smallest_node = heapq.heappop(min_heap)[2]
            current.next = smallest_node
            current = current.next 

            # if there is a next node in the list, add it to the heap
            if smallest_node.next:
                i = i + 1
                heapq.heappush(min_heap, (smallest_node.next.val, i,smallest_node.next))
        return dummy.next

# time O(Nlogk), where 𝑁 is the total number of nodes across all linked lists and 
# 𝑘 is the number of linked lists. The space complexity is O(k) for the heap.
