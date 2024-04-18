"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n > 0: 
            if not n%2:
                return self.myPow(x*x, n/2)
            else:
                return x * self.myPow(x*x, (n-1)/2)

        if n < 0: return 1/self.myPow(x, -n)

# O(logn)
# O(n)
        
# Optimized approach:

# Binary exponentiation, also known as exponentiation by squaring, is a technique for efficiently computing the power of a number. By repeatedly squaring xxx and halving nnn, we can quickly compute xnx^nx 
# n using a logarithmic number of multiplications.

# The basic idea here is to use the fact that x**n can be expressed as:
# if n is even, (x*x)**(n/2)
# if n is odd, x * (x*x)**((n-1)/2)


# This method might not seem intuitive, so let's try to understand it with the help of some examples 2^10.

# Using the previously discussed recursive approach we will have to multiply 2 in 100 steps.

# But using binary exponentiation, it will be reduced to about only 10 steps.
