"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10**4
1 <= Node.val <= 10**5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import ListNode, Optional
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     setA = set()
    #     while headA:
    #         setA.add(headA)
    #         headA = headA.next
    #     while headB:
    #         if headB in setA:
    #             return headB
    #         headB = headB.next 
    #     return 
    # # time O(m+n), m is the size of linkedlist A, n is the size of linkedlist B
    # # space O(m) size of linkedlist A      



"""Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?"""
    # space O(1) solution, use two pointers, difficulty is how to let p1 and p2 arrive at the interscation at the same time?
# Need to start the two pointers at the same length!
# 1. Calculate NNN; the length of list A.
# 2. Calculate MMM; the length of list B.
# 3. Set the start pointer for the longer list.
# 4. Step the pointers through the list together.
     
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     1,    2,        3
    #  M      head,1    head, 2     3
        M, N = 0, 0
        # find the length of linkedListA
        l1, l2 = headA, headB
        while l1:
            M += 1
            l1 = l1.next
        # find the length of linkedListB
        while l2:
            N += 1
            l2 = l2.next
        # find the start pointer of the longer linkedlist
        #   1  1, 2, 4
        #      8  2, 4
        # M - N = 1, index 1 is the start pointer of the longer linkedlist
        if M > N:
            start = headA
            for _ in range(M-N): # 0
                start = start.next
            # Step the pointers through the list together.
            p1, p2 = start, headB
            while p1 and p2:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next 
            return 
        elif N > M:
            start = headB
            for i in range(N-M):
                # print(i)
                start = start.next 
        # Step the pointers through the list together.
            p1, p2 = headA, start
            while p1 and p2:
                if p1 == p2:
                    return p1 
                p1 = p1.next
                p2 = p2.next 
            return 
        elif M == N:
            p1, p2 = headA, headB
            while p1 and p2:
                if p1 == p2:
                    return p1 
                p1 = p1.next
                p2 = p2.next 
    # time O(M+N)
    # space O(1)
        

    # the most optimized solution 
    # https://labuladong.online/algo/essential-technique/linked-list-skills-summary-2/#%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E6%98%AF%E5%90%A6%E7%9B%B8%E4%BA%A4
    # when headA is null, let headA points to LinkedListB
    # when headB is null, let headB points to LinkedListA
    # ------(listA)----listB
    # listB------(listA)----

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
        # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
        # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p1
