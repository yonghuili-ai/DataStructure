"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:

1 <= size <= 1000
-105 <= val <= 10**5
At most 10**4 calls will be made to next.

"""

from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.res = deque()
        

    def next(self, val: int) -> float:
        if len(self.res) + 1 <= self.size: 
            self.res.append(val)
            return sum(self.res)/len(self.res)
        else:
            self.res.popleft()
            self.res.append(val)
            return sum(self.res)/self.size

# Here, we could apply a data structure called double-ended queue (a.k.a deque) to implement the moving window, which would have the constant time complexity (O(1)) to add or remove an element from both its ends. 
# With the deque, we could reduce the space complexity down to O(N) where N is the size of the moving window.
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)