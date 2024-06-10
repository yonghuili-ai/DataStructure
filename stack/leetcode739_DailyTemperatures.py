"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]"""


# initial method, can jump to the templated method attached below
def dailyTemperatures(temperatures: list[int]):
    # since this question is asking about index, then push the index to the stack
    # compare the current tempareture with the stack top index corresponding tempareture, if current temperature is higher, then we find the day to get a warmer temperature. current index - stack top index is the day number. 
    # always need to append the current day's index to stack
    # result should be design as [0]*len(tempartures) to save each day's result
    res = [0] * len(temperatures)
    stack = []
    for i, v in enumerate(temperatures):
        while stack and v > temperatures[stack[-1]]:
        # means find the next warmer day, or the same as find the first day of trending up, the result at this index is 1
            idx = stack.pop()  
            res[idx] = i - idx  
        stack.append(i) # means if the temperature is going down, then append these indexes until going up again
    return res

from typing import List

# template solution
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    i = n - 1
    stack = []
    res = [0 for _ in range(n)]
    while i >= 0 :
        while stack and stack[-1][0] <= temperatures[i]:
            stack.pop()
        if stack and stack[-1][0] > temperatures[i]:
            res[i] = stack[-1][1] - i 
        # elif not stack:
        #     pass 
        stack.append((temperatures[i], i))
        i -= 1
    return res