"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

"""

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # comment out is a O(N) space solution, uncomment one is O(1) space solution
        # n = len(gain)
        # alt = [0 for _ in range(n+1)]
        # for idx in range(1, n+1):
        #     alt[idx] = gain[idx-1] + alt[idx-1]
        #     res = max(alt[idx], res)
        res = cur = 0
        for alt_gain in gain:
            # adding the gain in altitude to the current altitude
            cur += alt_gain
            # update the highest altitude
            res = max(res, cur)
        return res

# Here's how the Prefix Sum method works:

# Preprocessing: Iterate through the original array and compute the cumulative sum up to each index. Store these cumulative sums in a separate array.
# Querying: To compute the sum of elements in a subarray [i, j], you can simply subtract the cumulative sum at index i-1 from the cumulative sum at index j. This gives you the sum of all elements from index i to index j.

# def prefix_sum(arr):
#     n = len(arr)
#     prefix = [0] * (n + 1)  # Create a prefix sum array with an extra element
#     for i in range(1, n + 1):
#         prefix[i] = prefix[i - 1] + arr[i - 1]  # Compute cumulative sum
#     return prefix

# def range_sum(prefix, left, right):
#     return prefix[right + 1] - prefix[left]  # Compute sum of subarray [left, right]

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# prefix = prefix_sum(arr)
# print(range_sum(prefix, 1, 3))  # Output: 9 (sum of elements from index 1 to 3)