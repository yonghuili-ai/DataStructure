'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

import unittest

# The main code that you want to test

def isValid(s) -> bool:
    if len(s) == 1: return False
    # the parentheses decides only left ones can be put into stack
    # when the i is not the left one, need to pop from stack and compare, if match, then continue, else False
    # when stack is empty, and right is i, return False

# after all loop through, if any element left in stack, return False
    d = {'{':'}', '[': ']', '(':')'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif i not in d and len(stack) > 0:
            left = stack.pop()
            if d[left] != i: return False 
            else: continue
        elif i not in d and len(stack) == 0:
            return False
    return len(stack) == 0 

# Test cases for the add function
class TestAddFunction(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(isValid('(())'), True)

    def test_function_2(self):
        self.assertEqual(isValid('(('), False)

    def test_function_3(self):
        self.assertEqual(isValid('()[]{}'), True)

if __name__ == '__main__':
    unittest.main()