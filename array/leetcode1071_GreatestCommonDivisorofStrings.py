""" 
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2= len(str1), len(str2)
        res = ""
        def is_valid(idx):
            if l1 % (idx+1) or l2 % (idx+1):
                return False 
            # must be the same base here, str1 == str1[](base), and str2 = str1[](the same base)
            return str1 == str1[:idx+1] * (l1//(idx+1)) and str2 == str1[:idx+1] * (l2//(idx+1))
        for i in range(min(l1, l2)):
            if is_valid(i):
                print(i)
                res = str1[:i+1]
                print(res)
        return res 



