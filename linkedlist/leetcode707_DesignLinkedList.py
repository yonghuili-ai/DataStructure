"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

# summary: Find the predecessor of the node to insert!
# sentinal head, index = 0 for the first actual node

# Find the predecessor of the node to insert. If the node is to be inserted at the head, its predecessor is a sentinel head. If the node is to be inserted at the tail, its predecessor is the last node
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class MyLinkedList:

    def __init__(self):
        # self.head = None
        # must be a dummy node, otherwise when index = 0, self.addAtIndex(0, val) will call newNode = Node(val, prev.next). And prev is None, None does not have attribute 'next'
        self.head = Node(-1)
        # the reason to have size defined is from the hint of the requirement as:
        # void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: # size is always 1 more than the last index
            return -1
        curr = self.head
        for i in range(index + 1): # consider the sentinel head
            curr = curr.next
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        # Append a node of value val to the last element of the linked list.
        # If index equals the length of the linked list, the node will be appended to the end of the linked list. 
        # self.size is the current linked list size, before this index means the last node
        self.addAtIndex(self.size, val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        # Add a node of value val before the indexth node in the linked list
        if index < 0 or index > self.size: # notice: equal is allowed to insert before the indexth, which is the tail
            return 
        # find the predecessor
        prev = self.head
        for _ in range(index):
            prev = prev.next
        # add newNode between prev and prev.next
        newNode = Node(val)
        # the order of these two can not be reversed!
        # because we now find prev, and prev.next. First let new.next point to prev.next, 
        # then prev.next point to new 

        # the other way around is prev.next = newNode (means prev.next points to newNode), then newNode.next = prev.next (means new.next points to prev.next, which is new itself)

        # remember! always set where the newNode will points to first!
        newNode.next = prev.next
        prev.next = newNode
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        # this index could be head, tail or in between node
        # first check index
        if index < 0 or index >= self.size: 
            return 
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
        



        

# Insert the node by changing the links to the next and previous nodes.
# to_add.prev = pred
# to_add.next = succ
# pred.next = to_add
# succ.prev = to_add
# The original order or any order where you first set the new node's prev and next links before updating the adjacent nodes' links is safe.


# Delete the node by changing the links to the next and previous nodes.
# pred.next = succ
# succ.prev = pred
# reverse order also works.

# double linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1) # add tail is critical, otherwise, self.addAtIndex(0, val) and self.addAtIndex(self.size, val) will not work, because add node at head when linkedlist points to None. Adding a sentinel tail will avoid that problem
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index+1):
                cur = cur.next
        return cur.val
        
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
        

    def addAtTail(self, val: int) -> None:
        # Add a node of value val before the indexth node in the linked list
        # current last node index is self.size - 1, so the new tail index is self.size
        self.addAtIndex(self.size, val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        # before index node
        if index < 0 or index > self.size:
            return 
        pred = self.head
        new = Node(val)
        for _ in range(index): # loop end at the precessor
            pred = pred.next
        succ = pred.next 
        new.next = succ
        new.prev = pred
        succ.prev = new 
        pred.next = new
        self.size += 1





        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next.next # different from insertAtIndex succ = pred.next 
        pred.next = succ
        succ.prev = pred
        self.size -= 1