"""A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer."""
def validWordAbbreviation(word: str, abbr: str) -> bool:
    w, a = 0, 0
    while w < len(word)  and a < len(abbr): # using while loop which is easier to make index change
        # first check if abbr[a] is alpha
        if abbr[a].isalpha():
            if abbr[a] != word[w]:
                return False
            else:
                a += 1
                w += 1

        # second check if abbr[a] is digit
        elif abbr[a].isdigit():
            # check leading zero
            if abbr[a] == '0':
                
                return False 
            else:
                # get the potential multi-digits num
                num = 0
                # use the while loop which is easy to get all the continous digits in abbr
                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1
                # jump num index in word
                w += num 
                print(f"w is {w}, a is {a}")
                # then it will compare if the two chars from word and abbr matches in the if loop
        
        # after checking on the shortest length, w and a might not be the last index. In this case, the abbr is not valid.
        # Need to check if index is on the last in both word and abbr
    return w == len(word) and a == len(abbr)
# time O(n)
# space O(1)

word = "internationalization"
abbr = "i12iz4n"
print(validWordAbbreviation(word, abbr))