"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 10**4
0 <= prices[i] <= 10**4
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # key point is to consider every peak immediatedly following a valley to maximize the profit. 
        # in python, remember this pattern for loop once to find all consecutive valley and peak
        # while i < len(prices) - 1:
            # while i < len(prices) - 1 and price[i] > price[i+1] (going down):
                # i += 1 (this will find the minimal value at i+1)
            # valley = price[i] (this i is actually the i + 1 from previous)
            # while i < len(prices) - 1 and price[i] < price[i+1] (going up):
                # i += 1 (this will find the maximum value at i+1)
            # peak = price[i] (this i is actually the i + 1 from previous)
        i = max_p = 0
        n = len(prices)
        valley = peak = prices[0]
        while i < n - 1: 
            while i < n - 1 and prices[i] >= prices[i+1]: # must include = for [3,3] case
                i += 1
            valley = prices[i] # when i == n-1 the last element, by default it will be valley
            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]# when i == n-1 the last element, by default it will be peak, peak and valley could be the same element
            max_p += peak - valley
        return max_p

# O(n) time loop onece
# O(1) space



            