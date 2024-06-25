"""Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(node, res):
            if not node: return 
            res.append(node.val)
            traverse(node.left, res)
            traverse(node.right, res)
            return 

        traverse(root, res)
        return res 

# res is defined as a local variable within the method preorderTraversal of the class Solution. Here is a breakdown:

# res is initialized as an empty list within the preorderTraversal method.
# It is then passed as an argument to the nested function traverse.
# Inside traverse, res is modified by appending values to it.
# Finally, the preorderTraversal method returns res.

# time O(N)
# space O(N)