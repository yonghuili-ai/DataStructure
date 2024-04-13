import unittest

def minRemoveToMakeValid(s: str) -> str:
    # string is immutable, for convenience to change element, convert s to list
    l = list(s)
    # leverage property of stack to pop the topest, we save the open ( index to stack, when looping to see a closed ),
    # it is time to pop the top open ( out. 
    stack = []
    # if redundant close ) in the loop, change stack[idx] to empty
    # if redundant open ( left in the loop, change stack[idx] to empty
    # return a string by join the stack list
    for idx, char in enumerate(l):
        if char == "(": stack.append(idx)
        elif char == ")": 
            if stack: stack.pop()
            else: l[idx] = ""
        
    while stack:
        l[stack.pop()] = ""

    return "".join(l)

class TestAddFunction(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")

    def test_function_2(self):
        self.assertEqual(minRemoveToMakeValid("a)b(c)d"), "ab(c)d")

    def test_function_3(self):
        self.assertEqual(minRemoveToMakeValid("))(("), "")

if __name__ == '__main__':
    unittest.main()

