"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l, r):
            # base condition
            if l >= r: return
            # recursion relation
            if l < r:
                s[l], s[r] = s[r], s[l]
                print("before recursion s: ", s)
                helper(l+1, r-1)
                print("after recursion s: ", s)
        helper(0,len(s)-1)
    
Solution().reverseString(["h","e","l","l","o"])