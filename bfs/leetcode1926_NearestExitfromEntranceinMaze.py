"""
ou are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.

"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # how to define exits in maze?
        # if any index i or j is at the bounary and maze[i][j] == "." and not the same as entrance
        row, col = len(maze), len(maze[0])
        from collections import deque
        q = deque()
        q.append(entrance)
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        step = 0
        while q:
            step += 1
            for i in range(len(q)):
                cur_x, cur_y = q.popleft()
                if (cur_x == 0 or cur_y ==0 or cur_x == row -1 or cur_y == col -1) and maze[cur_x][cur_y] == "." and (cur_x != entrance[0] or cur_y != entrance[1]):
                    # return current step
                    return step - 1
                for nx, ny in directions:
                    n_x, n_y = cur_x + nx, cur_y + ny
                    if n_x >= 0 and n_x < row and n_y >= 0 and n_y < col and (n_x, n_y) not in visited and maze[n_x][n_y] != "+":
                        q.append((n_x,n_y))
                        visited.add((n_x,n_y))
        return -1

# Time complexity: O(m⋅n)
# Space comp: 
# We use a queue queue to store the cells to be visited. In the worst-case scenario, there may be O(m+n)bcells stored in queue.
