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

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# time O(m+n)
# space O(1)--only pointers

# summary, sentinel head and tail. Update tail to track the current node in merged linkedlist! ListNode of list1 in function arguments can be understood as the head of each linkedlist!


from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use the ListNode as the head! so list1 is actually the current head of each linkedlist
        # keep track of the head of the new Linkedlist, and the tail to add merged nodes
        head = ListNode(-1)
        tail = head

        while list1 and list2:
            if list1.val > list2.val: # compare the head values
                tail.next = list2 
                list2 = list2.next # update the head to next in list2
            else:
                tail.next = list1 
                list1 = list1.next # update the head of list1
            # update tail, 
            tail = tail.next 
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2 
        return head.next 
        
# Approach 2: Iteration
# Intuition

# We can achieve the same idea via iteration by assuming that l1 is entirely
# less than l2 and processing the elements one-by-one, inserting elements of
# l2 in the necessary places in l1.

# Algorithm

# First, we set up a sentinel "head" node that allows us to easily return the
# head of the merged list later. We also maintain a tail pointer, which
# points to the current node for which we are considering adjusting its next
# pointer. Then, we do the following until at least one of l1 and l2 points
# to null: if the value at l1 is less than or equal to the value at l2,
# then we connect l1 to the previous node and increment l1. Otherwise, we
# do the same, but for l2. Then, regardless of which list we connected, we
# increment prev to keep it one step behind one of our list heads.

# After the loop terminates, at most one of l1 and l2 is non-null.
# Therefore (because the input lists were in sorted order), if either list is
# non-null, it contains only elements greater than all of the
# previously-merged elements. This means that we can simply connect the
# non-null list to the merged list and return it.

