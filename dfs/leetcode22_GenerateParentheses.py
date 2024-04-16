"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtracking(left:int, right:int, s:str):
            # find solutions / Base case
            if len(s) == n*2:
                res.append(s)
                return 
            # iterate over all possible candidates
            else:
                if left > right: 
                    backtracking(left, right+1, s +')')
                if left < n:
                    backtracking(left+1, right, s+"(")
        backtracking(0,0, "")
        return res 
    
test = Solution()
print(test.generateParenthesis(4))
