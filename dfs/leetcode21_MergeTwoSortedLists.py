"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []


Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# recursion relation
# if list1[0] < list2[0] ==> list1[0]+ merge(list1[1:], list2) 
# if list1[0] > list2[0] ==> list2[0]+ merge(list1, list2[1:]) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # for linked list, we only know about head and next, so intuitively, we should return the head
        # the problem can break down into smaller node between the two head node, pointing to already sorted merged list from recursion function (and this recursion function should return head)
        # time complex O(m+n) m is nodes number in list1, n is nodes number in list2
        # space complex O(m+n) m is nodes number in list1, n is nodes number in list2
        if not list1: return list2 # here the list actually is the head node of each linked list
        if not list2: return list1 # always return the head, that is how linked list knows where to start, very different from array
        # recursion relation
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 # return the current head
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2 # return the current head, list2 is actually the head Node!


        