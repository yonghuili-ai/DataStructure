"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""



from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # keys = set()
        # for pre, key in enumerate(rooms):
        #     keys.update(key)
        #     if  len(key) == 0:
        #         continue
        #     if pre+1 not in keys:# this is not the sufficient logic
        #         return False
        # return True
        
        # DFS or stack
        # when visiting a room for the first time, look at all keys in that room. For any key that has not been used yet, add it into the todo list / stack for it to be used.
        visited = {0}
        stack = [0]
        while stack:
            cur = stack.pop()
            for key in rooms[cur]:
                if key not in visited:
                    stack.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)

# O(N+E) n number of rooms, e number of keys
# O(N) stack


        # BFS to traverse all the nodes/keys available, and check if len(keys) == len(rooms)
        # visited contains all the available keys so far
        # q should save the keys when go iterate over the rooms
        # n, visited, q = len(rooms), set(), deque()
        # visited.add(0)
        # q.append(0)
        # while q and len(visited) < n:
        #     cur = q.popleft()
        #     for key in rooms[cur]:
        #         if key not in visited:
        #             q.append(key)
        #             visited.add(key)
        # return len(visited) == n
        



        