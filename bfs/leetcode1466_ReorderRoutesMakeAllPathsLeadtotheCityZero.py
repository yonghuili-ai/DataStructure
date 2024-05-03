"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:

2 <= n <= 5 * 10**4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""
# time O(n) loop for adj is n, and queue is n
# space O(n)

from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # bfs to traverse the graph
        # direction in graph, need to record in-degree and out-degree 
        res = 0
        adj = [[] for _ in range(n)]
        # use the index in adj for node, and value is tuples in the list, store the neighbor node and indegree of the node.
        # [a,b] means a to b, therefore, the indegree of a is -1, and indegree of b is +1
        for from_node, to_node in connections:
            adj[from_node].append((to_node, -1))
            adj[to_node].append((from_node, 1))
        # use queue to traverse the non-directional graph 
        visited = {0}
        q = deque([0])
        while q:
            cur = q.popleft()
            # need to loop all the next level of cur
            for neigh, indegree in adj[cur]:
                if neigh not in visited:
                    # if indegree is -1, means the cur node / parent points to the neigh/child, which should be reversed, since all child should point to parent as question asked.
                    if indegree == -1:
                        res += 1
                    visited.add(neigh)
                    q.append(neigh)
        return res



        