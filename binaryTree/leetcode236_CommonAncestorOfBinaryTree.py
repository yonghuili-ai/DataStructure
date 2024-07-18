# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base condition, return p or q or none
        if root is None: return None
        # lca(node2, 5, 4) => lca(node7, 5, 4) = left, lca(node4, 5, 4) = right; root = q => return root => return node4
        if p == root or q == root: return root 
        
        # 无脑丢给左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # three conditions
        # condition 1, if left, right are returned with node, means the root is lca
        if left and right:
            return root
        # condition 3, if right, not left, means lca is on the right, two nodes are embedded
        if right:
            return right
        # condition 2, if left, not right, means lca is on the left, two nodes are embedded
        if left:
            return left
        
        
    # O(n) check on each node
    # O(h) or O(n) depth of recursion tree, worst O(n)