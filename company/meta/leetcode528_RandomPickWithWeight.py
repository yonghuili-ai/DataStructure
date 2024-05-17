"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 10**4
1 <= w[i] <= 10**5
pickIndex will be called at most 10**4 times.

"""


import random
class Solution:
# example of array/w as [1,2,3,4,3], as required, we need to pick an index of 0 with probabilty 1/13, and index of 1 with probability 2/13, and index of 4 with probability 3/13. Consider array with index as value with the total number as sum of all num in w, then it will be [0, 1,1,2,2,2,3,3,3,3,4,4,4]. 
# when use a random.random() function which returns random between 0 and 1, multiple by total sum, which range will it fall into? need to sum [0, 1,1,2,2,2,3,3,3,3,4,4,4] and find out. 
# then the problem changes to find the random returned target falls into which cumulative sum range and pick the left side. 
# time O(n) loop n times in constructure for cumulative sum array, and n time to find index
# space O(n) cumulative sum array
    def __init__(self, w: List[int]):
        self.w = w
        self.cum_sum = []
        curr_sum = 0
        for i in range(len(self.w)):
            curr_sum += self.w[i]
            self.cum_sum.append(curr_sum)
        self.total = self.cum_sum[-1]


        
    # since the self.cum_sum is an ordered array, we can use binary search to decrese the time complex to O(logN)
    def pickIndex(self) -> int:
        random_weight = random.random() * self.total
        left, right = 0, len(self.cum_sum) - 1
        while left < right:
            mid = left + (right - left) // 2
            if random_weight > self.cum_sum[mid]:
                left = mid + 1
            else:
                right = mid 
        return left
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()