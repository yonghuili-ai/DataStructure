# do not understand, put the answer and explaination here
"""
Explanation
We maintain a decreasing mono stack,
(I stored the index of elements)

As we iterate each element a in input array A,
assume the last element in the stack has index i.
If the last element A[i] <= a,
A[i] can see a,
so we increment res[i]++

Because a is tall and block the line of sight.
A[i] can't see any element after a,
we have done the work for A[i],
so we stack.pop() it from the stack.

We keep doing this while A[i] < a, where i = stack.top().
By doing this, if stack is not empty,
A[i] will be the left next greater element of a.
A[i] can still see a,
so we increment res[i]++.

We do the above for each element a in A,
and we finally return result res


Complexity
Time O(n)
Space O(n)

"""

class Solution:
    def canSeePersonsCount(self, A):
        res = [0] * len(A)
        stack = []
        for i, v in enumerate(A):
            # Because a is tall and block the line of sight.
            # A[i] can't see any element after a,
            # we have done the work for A[i],
            # so we stack.pop() it from the stack.
            while stack and A[stack[-1]] <= v:
                res[stack.pop()] += 1
            # We keep doing this while A[i] < a, where i = stack.top().
            # By doing this, if stack is not empty,
            # A[i] will be the left next greater element of a.
            # A[i] can still see a,
            # so we increment res[i]++.
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res