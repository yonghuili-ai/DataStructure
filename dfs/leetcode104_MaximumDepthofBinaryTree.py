# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        md = 0
        def dfs(root, md):
            if not root: return md
            if not root.left and not root.right: return md+1
            left_md = dfs(root.left, md+1)
            right_md = dfs(root.right, md+1)
            res = max(left_md, right_md)
            return res
        return dfs(root, 0)