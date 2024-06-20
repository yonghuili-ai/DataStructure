"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:
Input: head = [1,2]
Output: [2,1]


Example 3:
Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
from typing import Optional

# recursion
# O(n)
# O(n) recursion call takes N stack space
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            # only one node in the linked list
            return head 
        
        # recursion relation -- assume all the nodes after head is reversed, 1-> [3->2]
        # now 2 should point next to head, and 2, which is the new tail of reversed sublinkedlist is the original head.next. So head.next.next = head
        # and head.next = None, otherwise, head.next still points to 3
        reversedSublit = self.reverseList(head.next) # new head = reversedSublit
        head.next.next = head 
        head.next = None # break the cycle, last node point to null

        # set each recursion function to return the head of the new sublinkedlist, 
        return reversedSublit


    
# iteration method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# since in single linked list, a node does not have reference to its previous node, we must track the previous node.This previous node initially can be None. 3(curr).next = 2(prev)

# when the curr next point to prev node, we lost track to the next node. Therefore, we need to save the next node to a variable by using: next_node = curr.next 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # for reverse nodes, everytime, just 2 nodes!
        # # 1. create a test case, two nodes reverse, 1->2 change to 2->1
        # prevNode = None
        # currNode = head
        # nextNode = currNode.next 
        # # reverse
        # currNode.next = prevNode
        # # iterate
        # prevNode = currNode
        # currNode = nextNode
        # # currNode is none, return prevNode

        # # 2. create a test case with 4 nodes, 1->2->3
        # after 2->1 -> None, move all nodes 1 step to 3->2->prev
        # prevNode = currNode # 1 
        # currNode = nextNode # 2 
        # nextNode = 3

        # time O(n), space O(1)

        # initialize
        prevNode = None
        currNode = head
        while currNode: # check currNode is enough, since only need to reverse 2 nodes at 1 iteration, and currNode is the last one in the two nodes
            nextNode = currNode.next # should within the loop. Must before the currNode.next pointing to prev. Because needs to record this node first.
            # reverse
            currNode.next = prevNode
            prevNode = currNode # 1 # 2
            currNode = nextNode
        return prevNode # curr is none, prev is the new head


        