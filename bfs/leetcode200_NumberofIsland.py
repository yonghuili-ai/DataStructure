"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, visited, i, j)
                    count += 1
        return count 
    
    def bfs(self, grid, visited, i, j):
        q = collections.deque([(i,j)])
        visited.add((i,j))
        neis = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            node = q.popleft()
            for nei in neis:
                new_node = (node[0] + nei[0], node[1] + nei[1])
                if self.is_valid(new_node, visited, grid):
                    q.append(new_node)
                    visited.add(new_node)
        # print(visited)
        return 
            
        
    def is_valid(self, new_node, visited, grid):
        if new_node in visited:
            return False
        if new_node[0] < len(grid) and new_node[0] >= 0 and new_node[1] < len(grid[0]) and new_node[1] >= 0 and grid[new_node[0]][new_node[1]] == "1":
            return True 
        
        
        