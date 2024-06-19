"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10**4
0 <= lists[i].length <= 500
-10**4 <= lists[i][j] <= 10**4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

"""

# intuitive method, use arr-list then sort, create a new linkedlist with the value in sorted list

from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists:
            return None
        new = []
        for l in lists:
            while l: # loop through linkedlist
                new.append(l.val)
                l = l.next
        new.sort()
        head = ListNode(-1)
        cur = head
        for ele in new:
            cur.next = ListNode(ele)
            cur = cur.next 
        return head.next 

# time, O(NlogN), N is the total number of nodes in lists, collecting all nodes cost N, sort cost NlogN, creating linkedlist N
# space, O(N), sorting space, new linkedlist



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from collections import heapq
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [[]]: return None
        h = []
        for i, l in enumerate(lists):
            if l: # this is critical, one linkedlist could be None
            # this should work in Python 2, but return with error in Python 3 as: TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
            # one way to fix it is to introduct an ordering mechanism for heapq.
            # The problem while adding ListNode objects as tasks is that the Tuple comparison breaks for (priority, task) pairs if the priorities are equal and the tasks do not have a default comparison order. The solution is to store entries as 3-element list including the priority, an entry count, and the task.
                heapq.heappush(h, (l.val, i, l))
        head = ListNode(-1)
        p = head
        i = len(lists) # otherwise, could be conflict in while loop, if i starts from 0
        while h:
            # find the node with smallest val among the current k heads
            nextNode = heapq.heappop(h)[-1]
            # link to the newly constructed linkedlist
            p.next = nextNode
            # move pointer p to the last position for next nodes
            p = p.next
            # need to check if nextNode is not the tail, adds one more from its linkedlist.Garantee that the k heads are the smallest among all lists because each linkedlist is sorted. 
            if nextNode.next:
                heapq.heappush(h, (nextNode.next.val, i, nextNode.next))
                i += 1
        return head.next
# time O(logk) k is how many sorted linkedlist. each pop and push to priority queue takes o(logk), and the while loop go through N nodes

# space O(n) created a new linkedlist, O(k) for creating the priority queue      