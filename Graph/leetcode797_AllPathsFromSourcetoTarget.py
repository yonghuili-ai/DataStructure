"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""

# dfs
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # to find all possible paths, use backtracking to explore all nodes
        # list(A-list) is a shallow copy of the list of A
        res = []
        def dfs(node, path):
            if node == len(graph) - 1: 
                # print(path)
                res.append(list(path))
                return 
            for next in graph[node]:
                    path.append(next)
                    dfs(next, path)
                    path.remove(next)
        dfs(0, [0])
        return res
    
# bfs
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # the trick is to have a tuple in queue, where the first element is source, and second one is the current path
        source = 0
        target = len(graph) - 1
        q = deque()
        q.append((source, [0]))
        res = []
        while q:
            cur_node, cur_path = q.popleft()
            if cur_node == target:
                # foundn one path
                res.append(cur_path)
            for nei in graph[cur_node]:
                q.append((nei, cur_path +[nei])) # using cur_path.append(nei) will change the cur_path, and +[nei] will only create a new list
        return res
    
# time complexity
    