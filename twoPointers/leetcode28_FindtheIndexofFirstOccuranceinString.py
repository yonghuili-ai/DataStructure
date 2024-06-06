"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 10**4
haystack and needle consist of only lowercase English characters.
"""





# method 1 two pointer
# O(n) Time 
# O(1) space 
def strStr(haystack: str, needle: str) -> int:
    init, h, n = 0, 0, 0
    while h < len(haystack):
        if needle[n] == haystack[h]: # find possible match
            # print(n, h, needle[n], haystack[h])
            init = h
            while h < len(haystack) and n < len(needle) and needle[n] == haystack[h]:
                h += 1
                n += 1
                # print(h, n)
            if h - init == len(needle): return init
            else: # did not find the match with starting position init
                n = 0
                h = init + 1 # h move 
        else: # the initial of haystack did not match, move h
            h += 1
    return -1 
        
print(strStr("mississippi", "issip"))

haystack = "sadbutsad"
needle = "tsad"
print(strStr(haystack, needle))


haystack1 = "leetcode"
needle1 = "leeto"
print(strStr(haystack1, needle1))


# method 2 sliding window 
def strStr2(haystack: str, needle: str) -> int:
    n = len(needle)
    for h in range(len(haystack)-n+1):
        if haystack[h:h+n] == needle:
            return h 
    return -1

print(strStr2(haystack, needle))
print(strStr2(haystack1, needle1))
print(strStr2("mississippi", "issip"))