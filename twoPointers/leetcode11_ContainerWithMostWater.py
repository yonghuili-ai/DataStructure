"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brutal force
        # O(n**2) == 10 **10 > 10 **8 will Time Limit Exceeded
        # res = 0
        # for i in range(len(height)):
        #     left_h = height[i]
        #     for j in range(i+1, len(height)):
        #         right_h = height[j]
        #         area = min(left_h, right_h) * (j - i)
        #         res = max(area, res)
        # return res

        # a greedy solution using two pointers
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            area = (j-i) * min(height[j], height[i])
            res = max(area, res)


            # if we try to move the pointers at the higher line inwards, we won't gain any increase. By moving the shorter line could be a potention increase in area.
            if height[j] > height[i]: # move i
                i += 1
            else:
                j -= 1
        return res

