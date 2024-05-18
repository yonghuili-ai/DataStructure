# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 本质上是问： 是否存在拓扑排序，bfs topological order， use queue
        q = []
        count = 0
        indegree, edge = self.get_indegree(numCourses, prerequisites)
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.pop(0)
            count += 1
            # decrease indegree of all its neighbor
            for neighbor in edge[node]:
                indegree[neighbor] -= 1
                # add indegree 0 node to q
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
            
            
        
    def get_indegree(self, numCourses, pre):
        # initialize
        indegree = [0 for i in range(numCourses)]
        edge = {i:[] for i in range(numCourses)}
        for point_in, point_out in pre:
            indegree[point_in] += 1
            edge[point_out].append(point_in)
        return indegree, edge

            
        