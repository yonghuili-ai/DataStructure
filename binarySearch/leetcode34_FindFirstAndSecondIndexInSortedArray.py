"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
nums is a non-decreasing array.
-10**9 <= target <= 10**9
"""

def searchRange(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    if n == 0: return [-1, -1]
    # left boundary
    def search_left():
        l, r = 0, n-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        print(l)
        if l < 0 or l >= n: return -1
        if nums[l] == target: return l
        else: return -1

    # right boundary
    def search_right():
        l, r = 0, n-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        if r < 0 or r >= n: return -1
        if nums[r] == target: return r
        else: return -1

    return [search_left(), search_right()]

nums = [2,2]
target = 3
print(searchRange(nums, target)) 



# https://labuladong.online/algo/essential-technique/binary-search-framework/
# Binary search remember
def binary_search(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 找到目标值
            return mid
    # 没有找到目标值
    return -1

def left_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小右边界
            right = mid - 1
    # 判断是否存在目标值
    if left < 0 or left >= len(nums):
        return -1
    # 判断找到的左边界是否是目标值
    return left if nums[left] == target else -1

def right_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小左边界
            left = mid + 1
    # 判断是否存在目标值
    if right < 0 or right >= len(nums):
        return -1
    # 判断找到的右边界是否是目标值
    return right if nums[right] == target else -1
