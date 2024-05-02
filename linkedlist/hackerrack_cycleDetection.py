# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return . Otherwise, return .

Example

 refers to the list of nodes 

The numbers shown are the node numbers, not their data values. There is no cycle in this list so return .

 refers to the list of nodes 

There is a cycle where node 3 points back to node 1, so return .

Function Description

Complete the has_cycle function in the editor below.

It has the following parameter:

SinglyLinkedListNode pointer head: a reference to the head of the list
Returns

int:  if there is a cycle or  if there is not
Note: If the list is empty,  will be null.

"""

def has_cycle(head):
    d =set()
    curr = head
    while curr:
        if curr in d:
            return 1
        else:
            d.add(curr)
        curr = curr.next
    return 0