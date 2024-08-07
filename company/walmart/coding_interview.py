"""Q1: Rearrange given array of distinct integers from range 0 to n-1 (where n is size of array) with some missing numbers (it will be -1 instead of missing numbers) such a way that each element of the array will be equal to the index or -1 for missing numbers (a[i]= (i || -1)).
Example:
input = [-1, 3, 1, 0]
output = [0, 1, -1, 3]
"""

def find_missing(arr):
        
# in place?
# [-1, 3, 1, 0]  ==> [0, 1, -1, 3]
    if not arr: return []
    n = len(arr)
    i = 0
    while i < n:
        while arr[i] != i and arr[i] != -1:
            right_id = arr[i]
            arr[i], arr[right_id] = arr[right_id], arr[i]
        i += 1 
    print(arr)
    return arr 

# arr = [-1, 3, 1, 0]
# find_missing(arr)

# arr = [-1, -1, 1, 0]
# find_missing(arr)

# arr = [0]
# find_missing(arr)

arr = []
find_missing(arr)

# [-1, 3, 1, 0] i=0, n=4
# arr[i] arr[right_id] arr
# -1.     3            [-1, 3, 1, 0]
# 3       0            [-1, 0, 1, 3] i = 1
# 0       -1.          [0, -1, 1, 3] 
# i=2 1.  -1           [0, 1, -1, 3 ]
# i = 3 






# [0, 1, -1, 3] 
    # set = set() 
    # res = [0,1,.... n-1]
    # for loop:
    #     if 2 is not in arr:
    #     res[2] = -1
        
    
    #     if 1 in arr:
    #         pass 

    # [-1, 3, 1, 0] set(0,1,2,3) res=(0,1,-1,-1)
    # [-1, -1, 1, 0]
    # [0] set(0) 
    # [-5] set(0) res[0] = -1
    
    # O(n) time
    # O(n) space 


    
        
        
    
    
    
''' Q2
Construct all possible BSTs for keys from 1..N
For N = 2, there are 2 unique BSTs
     1               2  
      \            /
       2         1 

For N = 3, there are 5 possible BSTs
  1              3        3         2      1
    \           /        /        /  \      \
     3        2         1        1    3      2
    /       /            \                    \
   2      1               2                    3
'''

# 1 , 2, 3, m = 2 

# root 2, left 1,2-1=>1 right 2+1,3 =>3
# root.left = left 
# root.right = right 


# 1, 2, 3, 4, 5, m = 3
# root 2, left 1,3-1=>1,2 right 3+1,5 =>4,5
# root.left = left 
# root.right = right 

#       3
#     1 . 5
#     2.  5
#     1.  4
#     2.  4
    
    
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
        
def trees(s, e): # s means start, e means end 
    all_trees = []
    for i in range(s, e+1):
        left_tree = trees(s, i-1)
        right_tree = trees(i+1, e)
        for l in left_tree:
            for r in right_tree:
                # create my BST
                # need a root
                root = Node(i)
                root.left = l 
                root.right = r 
                all_trees.append(root)
    return all_trees 
def print_all(node):
    print(node.val)
    print_all(node.left)
    print_all(node.right)

def bst_find_all(N):
    res = trees(1,N)
    for node in res:
        print_all(node)
    # print(res)
    return res


    
N = 2
bst_find_all(N)

# time n*(2**n)
# space n*(2**n)