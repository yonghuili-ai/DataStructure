from collections import defaultdict
import heapq
from typing import List

# time O(nlogn)
# space O(n+k) n for hashmap, k for returning res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for ele in nums:
            d[ele] += 1
        h = []
        for key, v in d.items(): # o(logn) for reach push and pop, so the worst case is NlogN
            heapq.heappush(h, (-v, key)) # must use key, not k, because python remember this k variable and cause error in while k loop
        while k > 0:
            k -= 1
            res.append(heapq.heappop(h)[1])
        return res 

nums = [1,1,1,2,2,3]
k = 2
a = Solution()
print(a.topKFrequent(nums, k))


        