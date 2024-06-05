"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums contains distinct values sorted in ascending order.
-10**4 <= target <= 10**4

"""




def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r: # remmeber l <= r, exit condition is l = right + 1 ([r, l] ==> [l+1, l] empty)
        m = l + (r-l)//2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
    return l # or r + 1, while loop exit with l = r - 1


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


