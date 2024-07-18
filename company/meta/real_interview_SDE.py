# Q1:
# Given an integer array and an integer total target, return whether a contiguous sequence of integers sums up to target
# ===Example===

# [1, 3, 1, 4], 8 : True
# [1, 3, 1, 4], 7 : False

def is_valid(arr, target):
    if not arr: return False 
    n = len(arr)
    for i in range(n):
        res = 0
        flag = True
        for j in range(i, n):
            if flag: 
                res += arr[j]
                if res < target:
                    pass
                elif res == target:
                    return True
                elif res > target:
                    flag = False
    return False
arr = [1, 3, 1, 4]
target=7
print(is_valid(arr, target))

# [1,3,1,4] O(n**2) time, O(1) space

# Solution during the interview, wrong
# def sliding_window(arr, target):
#     if not arr: return False
#     if len(arr) == 1: 
#         if arr[0] == target: return True
#         else: return False 
#     l, r = 0, 0 
#     window_sum = arr[l:r+1]
#     while r < len(arr) or l < len(arr):
#         if window_sum < target:
#             if r >= len(arr):
#                 return False
#             r += 1
#             window_sum += arr[r]
#         elif window_sum == target:
#             return True 
#         elif window_sum > target:
#             if l >= len(arr):
#                 return False
#             window_sum -= arr[l]
#             l += 1
#     return False 

def sliding_window(arr, target):
    l, r = 0, 0
    window_sum = 0
    while r < len(arr):
        window_sum += arr[r]
        # using a while loop to solve this problem!
        while l <= r and window_sum > target:
            window_sum -= arr[l]
            l += 1
        if window_sum == target:
            return True
        r += 1
    return False 

test1 = [1, 3, 1, 4]

test2 = [9]#[1, 3, 1, 5]
target = 8
print(sliding_window(test2, target))


# test3 = [8] 8 

# test4 = [1,1,1] 2


# test5 = [0,0,0] 2

# test6 = [9], 8


# Q2:
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Binary Tree:

#      1            <---
#    /   \
#   2     3         <---
#    \  
#    5              <---
# Answer: [1, 3, 5]



#      1            <---
#    /   \
#   2     3         <---
#    \   /
#    5   4          <---
# Answer: [1, 3, 4]

from collections import deque
def nodes_seen(node):
    if not node: return []
    q = deque()
    q.append(node)
    res = [] 
    while q:
        num = len(q)
        for i in range(num):
            curr = q.popleft()
            if i == num - 1:
                res.append(curr.val) # [1]  [1,3] [1,3,5]
            if curr.left:
                q.append(curr.left) # [2,3] 
            if curr.right:
                q.append(curr.right)# [3,5]
    return res

# node 1 [1]
#      1            <---
#       \
#        3         <---
#       /
#      4          <---

#    1
#   2. 2
#  3 

# O(n) time
# O(n) n of nodes number space 