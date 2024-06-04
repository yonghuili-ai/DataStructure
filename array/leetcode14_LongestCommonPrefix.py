"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""
# time O(n*m) n is the average length of strs[i], m is how many string in strs
# space O(1)
def longestCommonPrefix(strs: list[str]) -> str:
    pre = ""
    for idx in range(len(strs[0])): # take the first word, and loop over its index
        curr = strs[0][idx] # use this char as standard to compare all rest words at this idx
        # then vertically checking all the rest words, i for tracking words, using idx from first word 
        for i in range(1, len(strs)):
            if idx < len(strs[i]) and strs[i][idx] == curr:
                continue
            else:
                return pre
        # when all the vertical checks passed,then we need to add the curr char to prefix
        pre += curr 
    # when finishing checking the first word, we have a prefix
    return pre 

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))

strs2 = ["flower","flow","flight"]
print(longestCommonPrefix(strs2))