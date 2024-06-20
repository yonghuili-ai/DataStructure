"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]


Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""
# recursion base case:
# if only 1 node, recursion finished

# if two nodes, 3, 4
# for example, 2, 3, 4, 5, 3-sublist start, 4-sublist end, 2-pred, 5-succ
# reverse step 2-> 4, 3->5, 4->3
# pred.next = end 
# start.next = succ 
# end.next = start 

# time complexity O(N) worst case to reverse the whole linked list
# Space Complexity: O(N) in the worst case when we have to reverse the entire list. This is the space occupied by the recursion stack.

# recursion method, not sure about m-1 step, O(N) time, O(N) space
# https://labuladong.online/algo/data-structure/reverse-linked-list-recursion/#%E4%B8%89%E3%80%81%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%80%E9%83%A8%E5%88%86

from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None 
        # need to define 5 variables: 3 from reverse linked list + 2 from connect and tail for m~n nodes reverse only
        prev_node = None
        curr_node = head
#         left = 2, right = 4
#         None   1   ->   2   ->   3   ->   4    ->  5
#         prev  curr
#               prev <-  curr <-   3   <-   4    ->  5
#               conn     tail 
                
#         when reverse end                  prev ->  5
        
#         reconnect 4 (prev) to 1(conn), 2(tail) to 5(next)
#         prev_node.next = conn _node
#         tail_node.next = next_node
        
    
        for _ in range(1, left): # move prev_node, curr_node to location
            prev_node = curr_node
            curr_node = curr_node.next 
        
        # record the conn_node and tail_node
        conn_node = prev_node
        tail_node = curr_node
        
        # reverse till the right node
        for _ in range(left-1, right):
            next_node = curr_node.next # remember the next node
            curr_node.next = prev_node # reverse 
            prev_node = curr_node
            curr_node = next_node 
        # after for, prev_node is at the right node location 
        
        # conn   tail
        # 1   <-  2 <- 3 <- 4 -> 5
        # 1   ->  4 -> 3 -> 2 -> 5 
        # reconnect to conn_node and tail_node
        # when left = 1, conn is None, prev is the head 
        if conn_node: 
            conn_node.next = prev_node
        else:
            head = prev_node
        tail_node.next = next_node 
        
        return head 
    
    # O(n) go over each node 
    # O(1) in place 
