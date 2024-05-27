"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 10**5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10**4 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        self.size += 1
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort() # nlogn, at most call 5*10**4, this method will out of time limits
        if self.size%2: return self.arr[(self.size-1)//2]
        else: 
            median = self.arr[(self.size-1)//2] + self.arr[(self.size+1)//2]
            return median/2
        

# Approach 2: Two Heaps

import heapq
class MedianFinder:

    def __init__(self):
        # needs two heaps, 
        # one to store the larger half and find the min, => min_heap
        # one to store the smaller half and find the max, => max_heap
        self.small,self.large = [], [] # self.small = self.large = [] will create issue as explained following
# a = b = []:

# a and b reference the same list.
# Changes to the list via a affect b, and vice versa.
# a, b = [], []:

# a and b reference different lists.
# Changes to the list via a do not affect b, and vice versa.
        


# https://leetcode.com/problems/find-median-from-data-stream/solutions/969081/python-two-heap-solution-with-full-explanation/
    # We have a max heap representing the sorted left half of the stream, and a min heap representing the sorted right half of the stream.
    # The tops of these heaps represent the middle of the stream so far.
    
    # To get the median:
    #     - if len(left) == len(right): return (left[0] + right[0]) / 2
    #     - elif len(left) > len(right): return left[0]
    #     - else: return right[0]
        
    # To add a number x:
    #     If x <= left[0], add to left. Else, add to right.
    #     If abs(len(left) - len(right)) > 1: rebalance heaps.
        
    # To rebalance:
    #     Pop an element from the bigger heap and add it to the smaller heap.
        
    # Adding a number: O(log n) time, as there could be at most 2 pushes and 1 pop (log n).
    # Finding the median: O(1), since we just look at the 0th elements of the heaps.
    # Space: O(n), since we store every element in the heaps.

    def addNum(self, num: int) -> None:
        if not self.small or num > -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        # rebalance
        if abs(len(self.large) - len(self.small)) > 1:
            if len(self.large) > len(self.small):
                smt = heapq.heappop(self.large)
                heapq.heappush(self.small, -smt)
            else:
                lgt = -heapq.heappop(self.small)
                heapq.heappush(self.large, lgt)
    



        

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0]-self.small[0])/2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




