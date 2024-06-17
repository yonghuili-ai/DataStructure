"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""

# summary: split the original linkedlist, use two pointers p1, p2 to tracek two seperated linkedlist. p1 saves nodes smaller than x, p2 saves nodes larger than x. Also needs sentinel heads for each linkedlist for returning, and concatenting.

# Time Complexity: O(n)

# We traverse the linked list once, making the time complexity linear in the size of the list.
# Space Complexity: O(1)

# We use constant extra space since we are only creating two dummy nodes and reusing the existing nodes in the linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode(-1)
        head2 = ListNode(-1)
        p1, p2 = head1, head2 
        while head:
            if head.val >= x:
                p2.next = head 
                p2 = p2.next 
            else:
                p1.next = head 
                p1 = p1.next 
            # head = head.next this will create a loop linkedlist, see https://labuladong.online/algo/essential-technique/linked-list-skills-summary-2/#%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E5%88%86%E8%A7%A3 for detailed explaination

            # a good way is to disconnect main linkedlist head
            temp = head.next
            head.next = None # disconnect the main linkedlist
            head = temp 
        p1.next = head2.next 
        return head1.next 
