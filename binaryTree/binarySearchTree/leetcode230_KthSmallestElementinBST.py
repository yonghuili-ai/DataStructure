"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 10**4
0 <= Node.val <= 10**4
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
# https://labuladong.online/algo/data-structure/bst-part1/#%E5%AF%BB%E6%89%BE%E7%AC%AC-k-%E5%B0%8F%E7%9A%84%E5%85%83%E7%B4%A0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = 0
        self.res = 0
        def traverse(node):
            if not node: return 
            traverse(node.left)
            # 中序遍历代码位置
            self.rank += 1
            # 找到第 k 小的元素
            if self.rank == k:
                self.res = node.val
            traverse(node.right)
        traverse(root)
        return self.res
# time O(k) traverse k times, once self.rank == k, end the traverse
# space O(k) takes k stack space  
