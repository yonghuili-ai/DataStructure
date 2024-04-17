"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Assuming the recursion would return the swapped remaining list of nodes, we just swap the current two nodes and attach the remaining list we get from recursion to these two swapped pairs. 
        def helper(head):
            # base condition
            if not head or not head.next: 
                return head
            # recursion relation
            # define two nodes for better readability
            first_node = head
            second_node = head.next
            # swap two nodes and point first_node next to recursion head
            first_node.next = helper(second_node.next)
            second_node.next = first_node
            return second_node
        return helper(head)
    
# O(N) time
# O(N) space for stack