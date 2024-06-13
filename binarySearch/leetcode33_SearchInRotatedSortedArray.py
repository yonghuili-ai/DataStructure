"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 10**4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10**4 <= target <= 10**4

"""

# alway find from the sorted half!
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for one rotated, at least half of the array is sorted
        # first needs to find which side is ordered
        # if arr[left] < arr[mid], then left is sorted
        # if arr[mid] < arr[right], then right is sorted:
        # by checking which half of the array is sorted, then using the sorted property to determine if the target lies in that half, we can effectively eliminate half of the array. 
            # if left half sorted, then check if target > arr[left] and target < arr[mid]. 
            #     if so, binary search in this half, by assigning right = mid -1 
            #     else, the target must be in the right half, so left = mid + 1
            # likewise the same for right
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            # print(l, r, mid)
            if nums[mid] == target: return mid
            # if left half sorted
            if nums[l] <= nums[mid]:
                # check if target in left half 
                if target == nums[l]: 
                    return l
                elif nums[mid] > target > nums[l]:
                    r = mid - 1
                elif target == nums[mid]:
                    return mid
                # if not, then target is in the right half
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]: # right half is sorted
                # check if target in the right half
                if target == nums[mid]:
                    return mid
                elif nums[r] > target > nums[mid]:
                    l = mid + 1
                elif target == nums[r]:
                    return r
                # if not, then target is in the left half
                else: 
                    r = mid - 1
        return -1    

# time O(logn)
# space O(1)