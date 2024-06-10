"""For these questions, remember we should use a mono-increase or mono-decrese in the stack， similar questions are 739, 496, 503"""

"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
"""
# O(n) time,  given array once.
# Each building's index can be pushed to answer and popped from answer at most once, and both of the operations take O(1)O(1)O(1) time.
# Space complexity: O(N)
import unittest
def findBuildings(heights: list[int]) -> list[int]:
    # only the tallest and its right can see, use stack to get the tallest and descending ones
    stack  = []
    for idx, h in enumerate(heights):
        while stack and h >= heights[stack[-1]]: # use while loop to keep poping its left shorter ones, which does not have view
            stack.pop()
        # append the ones have view
        stack.append(idx)

    return stack 


class TestAddFunction(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(findBuildings([2,2,2,2]), [3])

    def test_function_2(self):
        self.assertEqual(findBuildings([4,3,2,1]), [0,1,2,3])

    def test_function_3(self):
        self.assertEqual(findBuildings([1,3,2,4]), [3])


if __name__ == '__main__':
    unittest.main()

# follow up question 1, can you complete with O(1) space?
"""
Algorithm

1. Initialize maxHeight to -1. It will store the maximum height of the buildings to the right of the current building.
2. Iterate over the buildings array from right to left.
If the current building is taller than maxHeight, then append its index to the answer array and update maxHeight with the current building's height.
3. At the end, the answer array has the indices of the buildings that can see the ocean in descending order.
4. Reverse the answer array (to make it in ascending order) and return it.
"""

class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = []
        max_height = -1
        
        for current in reversed(range(n)):
            # If there is no building higher (or equal) than the current one to its right,
            # push it in the answer array.
            if max_height < heights[current]:
                answer.append(current)
            
                # Update max building till now.
                max_height = heights[current]
        
        answer.reverse()
        return answer

# follow up question 2:  if we have an ocean view from both sides , ie : left and right . how do we do it in one pass?

def findBuildings(heights):
    n = len(heights)
    left, right = 0, n - 1
    left_max, right_max = heights[0], heights[n - 1]
    left_res, right_res = [0], [n - 1]
    """
    each step:
    1. compare left_max and right_max, move the pointer with smaller height , let's say we move right pointer: right -= 1
    2. compare heights[right] with right_max, if it doesnt have a view from right, it certainly won't have a view from left as left_max > right_max
    3. do the same thing until left == right
    """
    def findBuildings(heights):
        n = len(heights)
        left, right = 0, n - 1
        left_max, right_max = heights[0], heights[n - 1]
        left_res, right_res = [0], [n - 1]
        """
        each step:
        1. compare left_max and right_max, move the pointer with smaller height , let's say we move right pointer: right -= 1
        2. compare heights[right] with right_max, if it doesnt have a view from right, it certainly won't have a view from left as left_max > right_max
        3. do the same thing until left == right
        """
        while left < right:
            if left_max < right_max:
                left += 1
                if heights[left] > left_max and left< right:
                    left_res.append(left)
                    left_max = heights[left]
            else:
                right -= 1
                if heights[right -1] > right_max and left< right:
                    right_res.append(right)
                    right_max = heights[right]
        return left_res + right_res[::-1]    


"""variant of the above question
Given an array called nums, can you return a same length array which saves the next greater element for the corresponding element in each index of nums. If there is no next greater element, return -1.  

Example:

input nums = [2,1,2,4,3]
output [4,2,4,-1,-1]

input nums = [4,3,2,1]
output [-1,-1,-1,-1]


input nums = [7,7,8,8]
output [8,8,-1,-1]
"""

def nextGreaterElement(nums):
    n = len(nums)
    i = n-1
    stack = []
    res = [-1 for _ in range(n)]
    while i >= 0:
        while stack and stack[-1][0] <= nums[i]:
            # the top of stack is not greater than current element, needs to dig dipper in stack. Since stack is an strickly increasing from bottom to top 
            stack.pop()

        if stack and stack[-1][0] > nums[i]: 
            # found the next greater element
            res[i] = stack[-1][0]
            # add the current element to stack, which might be the next greater element for future loops
            stack.append((nums[i], i))
        elif not stack:
            stack.append((nums[i], i))
        else:
            pass
        i -= 1
    return res 

nums1 = [2,1,2,4,3]
nums2 = [4,3,2,1]
nums3 = [7,7,8,8]

print(nextGreaterElement(nums1))
print(nextGreaterElement(nums2))
print(nextGreaterElement(nums3))