"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

"""

# The solution is very simple. We can find out the extra maximum number of flowers, countcountcount, that can be planted for the given flowerbedflowerbedflowerbed arrangement. To do so, we can traverse over all the elements of the flowerbedflowerbedflowerbed and find out those elements which are 0(implying an empty position). For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next adjacent positions respectively.

# If the countcountcount obtained is greater than or equal to nnn, the required number of flowers to be planted, we can plant nnn flowers in the empty spaces, otherwise not.

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        num = 0
        if n == 0: return True 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # must check left and right empty when the current value is 0, otherwise, will get wrong result
                # left pot empty
                left_pot_empty = (i==0) or (flowerbed[i-1] == 0)
                # check if right pot is empty
                right_pot_empty = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left_pot_empty and right_pot_empty:
                    # also need to update the pot value
                    flowerbed[i] = 1
                    num += 1
        print(num)
        return num >= n
            

