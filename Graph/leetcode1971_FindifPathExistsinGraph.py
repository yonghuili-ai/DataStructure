"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 10**5
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""

# BFS 
# time complex O(V+E) O(V) for queue, O(E) for graph hashmap
# Space O(V+E) graph hashmap O(E), O(V) for queue, 
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        q = deque([source])
        visited = {source}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # print(graph)
        while q:
            cur = q.popleft()
            if cur == destination: return True 
            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False 
    

class Solution:
    # DFS
    # O(V+E) V for traverse all nodes, E for graph iteration
    # O(V+E) V is for visited set, E is for graph, V is for stack
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        # if n == 1 and source != destination: return False
        graph = defaultdict(list)
        # q = deque([source])
        visited = {source}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            # Use a visited set to keep track of nodes that have been visited during the traversal to avoid revisiting and potential infinite loops (cycles).
            for nei in graph[node]:
                if nei not in visited:
                    # visited.add(nei)
                    # print("current nei: ", nei)
                    # print("current visited: ", visited)
                    # If any recursive call returns True, propagate True back up through the call stack indicating that a path to the destination has been found.
                    if dfs(nei, visited):
                        return True

                    # visited.remove(nei)
            return False 
        return dfs(source, visited)


        