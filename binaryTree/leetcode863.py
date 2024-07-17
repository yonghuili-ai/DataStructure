# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        
        # Build a graph representation of the tree
        graph = defaultdict(list)
        # converts the binary tree into a graph using an adjacency list. Allow us to easily traverse the tree in all direction, both child to parent and parent to child.
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)
        # recursively builds the graph
        build_graph(root, None)
        
        # Perform BFS from the target node
        queue = deque([(target.val, 0)])
        seen = {target.val}
        result = []
        
        while queue:
            current, distance = queue.popleft()
            if distance == k:
                result.append(current)
            elif distance < k:
                for neighbor in graph[current]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return result  

# time O(n), we visited each node to build the graph and perform BFS
# space O(n), for storing the graph and BFS queue