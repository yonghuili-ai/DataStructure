# recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            # only one node in the linked list
            return head 
        # recursion relation
        reversedSublit = self.reverseList(head.next)
        head.next.next = head # append the head to the last, head.next is pointing to end of the reversedSublit, change the direction by using another .next to point back to head
        head.next = None # break the cycle, last node point to null
        return reversedSublit

# O(n)
# O(n)
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode 2  \ ListNode 3 \  ListNode 4
        # .next        \.next        \.next 
        # 
        # since in single linked list, a node does not have reference to its previous node, we must track the previous node.This previous node initially can be None. 3(curr).next = 2(prev)

        # when the curr next point to prev node, we lost track to the next node. Therefore, we need to save the next node to a variable by using: next_node = curr.next 
        prev = None # initialize prev
        curr = head
        while curr:
            next_node = curr.next # iterate next_node value 
            curr.next = prev 

            prev = curr # iteration
            curr = next_node # iteration
        return prev  # curr is none, prev is the head
# O(n)
# O(1)