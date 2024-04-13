import unittest

# The main code that you want to test

def basicOperator(s) -> int:
    curr, operator, stack = 0, "+", []
    operators = ("+", "-", "*", "/")
    s.replace(" ", "")        
    for i, char in enumerate(s):
        # if char == ' ': continue # not working for " 3/2 "
        if char.isdigit(): curr = 10 * curr + int(char)
        # here must use if, to handle the last element/char in s, which is a digit, and also need to handle the operators
        # the last element needs to check operator, that is why need i == len(s) - 1
        if char in operators or i == len(s) - 1: 
            if operator == "+":
                stack.append(curr)
            elif operator == "-":
                stack.append(-curr)
            elif operator == "*":
                stack.append(stack.pop() * curr)
            elif operator == "/":
                stack.append(int(stack.pop() / curr))
            operator = char
            curr = 0
        # print(stack)
    return sum(stack)
# example 3*2+1
# char, curr, operator, stack
        # 0       +       []
#   3     3       +       []
#   *     3       +       [3]
#loop end 0       *        
#   2     2       *       [3]
#   +     2       *       [3*2]
#loop end 0       + 
#   1     1       +  
#last     1       +       [3*2, 1]
# end loop  

class TestAddFunction(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(basicOperator('3+4/2'), 5)

    def test_function_2(self):
        self.assertEqual(basicOperator(' 3/2 '), 1)

    def test_function_3(self):
        self.assertEqual(basicOperator('10-4+2*3+10/5+1'), 15)

if __name__ == '__main__':
    unittest.main()