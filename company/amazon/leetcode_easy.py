# leetcode 2357. Make Array Zero by Subtracting Equal Amounts
"""
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

 

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # if sum(nums) == 0: return 0
        # count = 0
        # flag = True
        # while flag: 
        #     min_pos = float('inf')
        #     for i in nums:
        #         if i > 0:
        #             min_pos = min(i, min_pos)
        #         # print(min_pos)
        #     for idx, val in enumerate(nums):
        #         if val != 0:
        #             nums[idx] = val - min_pos
        #     # print(nums)
        #     count += 1
        #     if sum(nums) == 0:
        #         flag = False
            
        # return count
        # simplified version, each different number needs one operation
        dedup = set()
        for i in nums:
            if i > 0:
                dedup.add(i)
        return len(dedup)



# leetcode 1710. Maximum Units on a Truck
    """
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

 

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 10**6
 """   
"""Complexity Analysis

Time Complexity : O(nlog⁡n, where n is the number of elements in array boxTypes.

Sorting the array boxTypes of size n takes (nlog⁡n)vtime. Post that, we iterate over each element in array boxTypes and in worst case, we might end up iterating over all the elements in the array. This gives us time complexity as O(nlog⁡n)+O(n)=O(nlogn).

Space Complexity: O(1)\mathcal{O}(1)O(1), as we use constant extra space.
    """    
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        order = []
        boxTypes.sort(key=lambda x: x[1], reverse = True) # sort is in place, sorted(boxTypes, key, reverse) returns a new sorted list
        res = 0
        # print(boxTypes)
        for box, unit in boxTypes:
            if truckSize <= 0:
                break
            if truckSize - box > 0:
                res += box * unit
                truckSize -= box
            else:
                res += truckSize * unit
                truckSize = 0
        return res
     
# leetcode 14 Longest Common Prefix 
    
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_str = min(strs, key=lambda x: len(x))
        # print(min_str)
        res = ''
        for idx, char in enumerate(min_str):
            for word in strs:
                if word[idx] != char:
                    return res
            res += char
        return res 

        # O(n**2+nlogn)
        # O(1)
    


# needs review! leetcode 121. Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 10**5
0 <= prices[i] <= 10**4

"""
# two pointers
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # find the minimual on the left, as long as right is larger than the left, calculate the max. If right is smaller than left, l = r and check if there is bigger profix. max profix is always recorded in max_profit.
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit

# O(n)
# O(1)
    

# leetcode 1603. Design Parking System -- Easy no need to review

# leetcode 733 Flood Fill
    """can be done using both bfs and dfs"""
    """BFS"""
from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # typical BFS since it is a connected matrix
        q = deque()
        q.append([sr,sc])
        # print(q)
        visited = {(sr,sc)}
        row_upper, row_lower = 0, len(image) - 1
        col_upper, col_lower= 0, len(image[0]) -1
        neis = ((-1,0),(1,0),(0,1),(0,-1))
        while q:
            curr = q.popleft()
            # print(curr)
            original = image[curr[0]][curr[1]]
            image[curr[0]][curr[1]] = color

            for nei in neis:
                next_x = curr[0] + nei[0]
                next_y = curr[1] + nei[1]
                if next_x >= row_upper and next_x <= row_lower and next_y >= col_upper and next_y <= col_lower and original == image[next_x][next_y] and (next_x,next_y) not in visited:
                    q.append([next_x, next_y])
                    visited.add((next_x, next_y))

        return image
    
    """dfs not quite figure out yet""" 


        


    