"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 10**4
s1 and s2 consist of lowercase English letters.
"""
# To solve the problem of checking if s2 contains a permutation of s1, we can use the sliding window approach along with character frequency counting.


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False
        s1_count = Counter(s1)
        window_count = Counter(s2[0:len1])
        if s1_count == window_count: return True
        # sliding window to include one letter, and remove one letter 
        for i in range(len1, len2):
            window_count[s2[i]] += 1
            window_count[s2[i-len1]] -= 1
            # need to avoid cases like Counter({'o': 2, 'e': 0, 'i': 0, 'd': 0, 'b': 0, 'a': 0}) != Counter({'o': 2})
            if window_count[s2[i-len1]] == 0:
                # remove key, value pair from dictionary
                del window_count[s2[i-len1]]
            # check if current window_count the same as s1_count
            if window_count == s1_count: return True
        return False
# time O(n) loop s2 n letter once
# space O(n) dictionary counter 

        