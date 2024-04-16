# Definition for a binary tree node.
import math 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        return self.dfs(root, low=-math.inf, high=math.inf)
    
    def dfs(self, node, low, high):
        if node is None: return True
        if node.val >= high or node.val <= low: return False 
        # return self.dfs(node.left, -math.inf, node.val) and self.dfs(node.right, node.val, math.inf) this is wrong because it will not pass the correct low or high at one level down, must use low and high as below
        return self.dfs(node.left, low, node.val) and self.dfs(node.right, node.val, high)

# ? how to construct test case