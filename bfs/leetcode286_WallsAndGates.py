"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Example2:
Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        visited = set()
        row, col = len(rooms), len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            for i in range(len(q)):
                curr_x, curr_y = q.popleft()
                for dx,dy in direction:
                    next_x, next_y = curr_x + dx, curr_y + dy
                    if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and rooms[next_x][next_y] != -1 and (next_x, next_y) not in visited:
                        rooms[next_x][next_y] = rooms[curr_x][curr_y] + 1
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
        return rooms

# O(row*col) elements/nodes to iterate over, time
# O(row*col) max size of the queue, space  
            
        


        