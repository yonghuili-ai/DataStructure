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



