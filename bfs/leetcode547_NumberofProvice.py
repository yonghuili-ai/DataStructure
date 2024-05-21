"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""




# BFS

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # convert matrix to graph with neighbor
        n = len(isConnected)
        if n == 1: return 1
        # stardard method, convert any type to a {node: [list of neighbors]} format, and then traverse each neighbor
        # the difference for this problem is, you need to find the neighbor relation from the matrix isConnected.
        abj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n): # symmetric matrix, only need to compare the right top corner
                if isConnected[i][j] == 1: # get connected neighbor at both index
                    abj[i].append(j)
                    abj[j].append(i)
        # bfs
        res = 0
        visited = set()
        q = deque()
        for i in range(n):
            if i not in visited:  # means this i is not connected to the previous connected nodes, therefore, res+1
                q.append(i)
                visited.add(i)
                res += 1
            else: continue
            while q:
                cur = q.popleft()
                for neigh in abj[cur]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
        return res
            

 # Time O(n*n)
 # space O(n*n) for the graph list                   











# DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, isConnected, visited):
            visited.add(node)
            for i in range(len(isConnected)):
                # only need to check on 1 dimension, since no direction
                if isConnected[node][i] == 1 and i not in visited: # if the two are connected, then continue the recursion, until loop to the end of available node
                    dfs(i, isConnected, visited)
        # main function          
        res = 0
        visited =set()
        for i in range(len(isConnected)): # althrough it is a matrix, but here we only need to find all nodes are connected from 1-n
            if i not in visited:
                res += 1
                dfs(i, isConnected, visited)
        

        return res
# O(n*n) time
# O(n) set   
        