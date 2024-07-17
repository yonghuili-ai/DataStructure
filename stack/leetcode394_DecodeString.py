"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""

# To decode an encoded string that follows the pattern 𝑘[encoded_string], we can use a stack-based approach. The idea is to iterate through the string, pushing characters and numbers onto stacks until we encounter a closing bracket ], at which point we start decoding the string segment within the brackets. 


# Steps:
# Iteration: We iterate over each character in the input string.
# Digits: When we encounter a digit, we update current_num to accumulate the full number.
# Opening Bracket [:
# Push the current string (current_str) and the current number (current_num) onto the stack.
# Reset current_str and current_num for processing the new substring within the brackets.
# Closing Bracket ]:
# Pop the top element from the stack, which gives us the previous string and the number.
# Update current_str by repeating it num times and appending it to prev_str.
# Characters: If the character is a letter, we simply add it to current_str.
# Result: After the iteration is complete, current_str will contain the decoded string.

def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
    
    return current_str

# Example usage:
print(decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"

# time O(n) iterate through the string, stack push and pop O(1)
# space O(n) stack storage