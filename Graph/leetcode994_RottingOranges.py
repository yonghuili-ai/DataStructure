"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4


Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        res = 0
        
        q = deque()
        visited =set()
        count_1 = 0
        # get all rotton orange at min 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    count_1 += 1
        # print(count_1)
                    
        if count_1 == 0: return res
        while q:
            res += 1
            for i in range(len(q)):
                # print("current len(q): ", len(q))
                # print("current i: ", i)
                cur = q.popleft()
                
                for dir in {(0,1),(0,-1),(1,0),(-1,0)}:
                    nx, ny = cur[0] + dir[0], cur[1] + dir[1]
                    if (nx, ny) not in visited and nx >=0 and nx < len(grid) and ny >=0 and ny < len(grid[0]) and grid[nx][ny] == 1:
                        visited.add((nx,ny))
                        q.append((nx, ny))
                        grid[nx][ny] == 2
                        count_1 -= 1
                        if count_1 == 0: 
                            return res
        return -1 


        