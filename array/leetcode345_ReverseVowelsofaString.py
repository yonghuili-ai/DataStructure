# also need to use two pointers

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters."""

class Solution:
    def reverseVowels(self, s: str) -> str:
        option = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] not in option:
                l += 1
            elif s[r] not in option:
                r -= 1
            elif s[l] in option and s[r] in option:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)