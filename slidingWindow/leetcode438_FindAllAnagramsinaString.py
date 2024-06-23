"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 10**4
s and p consist of lowercase English letters.
"""
# time O(len_s), compare counter_p and counter_s is O(1) because at most 26 letters
# space O(len_s), counter is O(1) because at most 26 letters, results worst case len_s 

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        res = []
        len_p, len_s = len(p), len(s)
        # edge case
        if len_p > len_s: return res 
        # Initial window counter for the first window in s
        s_count = Counter(s[0:len_p])
        # check if the first window is an anagram of p
        if p_count == s_count: res.append(0)

        # sliding window over the rest index
        for i in range(len_p, len_s):
            # print(i, s_count, p_count)
            # add the new character to the current window counter
            s_count[s[i]] += 1
            # remove the character that is left behind as the window moves
            s_count[s[i-len_p]] -= 1
            # if the count becomes 0, remove it from counter for better efficiency
            if s_count[s[i-len_p]] == 0:
                del s_count[s[i-len_p]]
            
            # check if the current window is an anagram
            if s_count == p_count:
                res.append(i-len_p+1) # need to find the left index, which is i-len_p+1
        # print(res)
        return res
            