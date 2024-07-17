"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #     # similar to leetcode 27, delete duplicated elements in sorted array in place
        # s, f = 0, 0 
        # while f < len(nums):
        #     if nums[f] != val:
        #         nums[s] = nums[f]
        #         s += 1
        #     f += 1
        # return s
        k = 0  # Pointer for the position of the next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
# Initialization: We initialize a pointer k to 0. This pointer will keep track of the position where the next non-val element should be placed.

# Iteration: We iterate through the array using a loop. For each element:

# If the current element (nums[i]) is not equal to val, we place it at the position k and increment k.
# Return Result: After the loop completes, k will represent the number of elements in nums which are not equal to val. The elements from nums[0] to nums[k-1] are the required elements.

def twopointers_inplace_template(nums, val):
    if not nums: return []
    s, f = 0, 0
    while f < len(nums):
        if nums[s] == val:
            if nums[f] == val:
                f += 1
            elif nums[f] != val:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
                f += 1 
        elif nums[s] != val:
            s += 1
            # f = s + 1 wrong at [3,3] val = 5
            f = s
    print(nums)
    return nums

twopointers_inplace_template([3,2,2,3], 3)

