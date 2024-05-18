# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
# Giving a 2D array, find the first Kth smallest sum if you can choose one element from each of the array.
# Input:
# [[5, 4, 6, 6, 7],
# [1, 3, 3, 5, 9],
# [1, 1, 4, 5, 8]],
# K = 5 Output: (4 + 1 + 1, 4 + 1 + 1, 5 + 1 + 1, 5 + 1 + 1, 6 + 1 + 1) → 6, 6, 7, 7, 8

from heapq import *
def find_kth(arrs, K):
    h = []
    visited = set()
    res = []
    curr_sum = 0
    curr_idx = [0 for _ in range(len(arrs))] # the index of each row
    for arr in arrs:
        arr.sort()
        curr_sum += arr[0]
        
    print(arrs)
    print(curr_sum)
    h.append((curr_sum, curr_idx))
    visited.add(tuple(curr_idx))

    while len(res) < K:
        curr_sum, curr_idx = heappop(h)
        res.append(curr_sum)
        # add all possible solutions with idx + 1 for each row
        for i in range(len(arrs)):
            # copy the curr_idx
            next_idx = curr_idx[:]
            next_idx[i] = curr_idx[i] + 1
            
            if tuple(next_idx) not in visited:
                visited.add(tuple(next_idx))
                next_sum = curr_sum - arrs[i][curr_idx[i]] + arrs[i][next_idx[i]]
                h.append((next_sum, next_idx))
    return sorted(res)


arrs = [[5, 4, 6, 6, 7], [1, 3, 3, 5, 9], [1, 1, 4, 5, 8]]
K = 5
print(find_kth(arrs, K))
    


# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
# Giving a 2D array, find the first Kth smallest sum if you can choose one element from each of the array.
# Input:
# [[5, 4, 6, 6, 7],
# [1, 3, 3, 5, 9],
# [1, 1, 4, 5, 8]],
# K = 5 Output: (4 + 1 + 1, 4 + 1 + 1, 5 + 1 + 1, 5 + 1 + 1, 6 + 1 + 1) → 6, 6, 7, 7, 8

from heapq import heappop, heappush
class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        curr_sum = 0
        for row in mat:
            row.sort()
            curr_sum += row[0]
        curr_idx = [0 for _ in range(len(mat))]
        h = [(curr_sum, curr_idx)]
        visited = set(tuple(curr_idx))
        while k > 0:
            curr_sum, curr_idx = heappop(h)
            k -= 1
            for i in range(len(mat)):
                next_idx = curr_idx[:]
                if curr_idx[i] + 1 < len(mat[0]): # the next_idx[i] (which is curr_idx[i] + 1) max is len(mat[0]) - 1 
                    next_idx[i] = curr_idx[i] + 1
                    if tuple(next_idx) not in visited:
                        visited.add(tuple(next_idx))
                        next_sum = curr_sum - mat[i][curr_idx[i]] + mat[i][next_idx[i]]
                        heappush(h, (next_sum, next_idx))
                        # h.append((next_sum, next_idx)) # this is wrong since it will not use the heap structure but a list structure
        if k == 0: return curr_sum
        


        


mat = [[5, 4, 6, 6, 7], [1, 3, 3, 5, 9], [1, 1, 4, 5, 8]]
k = 5
a = Solution()
print(a.kthSmallest(mat, k))
    



