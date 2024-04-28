"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 10**5
s consists of lowercase English letters.
1 <= k <= s.length

"""
# the same as leetcode 643, O(n), O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        k_count = 0
        v = {'a','e','i','o','u'}
        # initial the sliding window
        for i in range(k):
            if s[i] in v:
                k_count += 1
        res = k_count
        for j in range(1, n-k+1):
            if s[j-1] in v:
                k_count -= 1
            if s[j+k-1] in v:
                k_count += 1
            res = max(k_count, res)
        return res