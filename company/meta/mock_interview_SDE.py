# Question, how to design your test case?
"""
You are given an array of integers. Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements. The algorithm should operate in place, i.e. shouldn't create a new array. The order of the nonzero elements does not matter. The numbers that remain in the right portion of the array can be anything. Example: given the array [ 1, 0, 2, 0, 0, 3, 4 ], a possible answer is [ 4, 1, 3, 2, ?, ?, ? ], 4 non-zero elements, where "?" can be any number. Code should have good complexity and minimize the number of writes to the array.
""""

[ 1, 4, 2, 3, 0, 0, 0 ]
              l  r

# wrong solution, see leetcode283 in twoPointers
def swap(nums):
    # edge
    if len(nums) == 1 and nums[0] != 0: return 1
    if len(nums) == 1 and nums[0] == 0: return 0
    if not nums: return 0

    l, r = 0, len(nums)-1 # 0, 6
    res = 0
    while l < r:
        if nums[l] != 0 and nums[r] == 0:
            pass
        elif nums[l] == 0 and nums[r] != 0:
            # swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] == 0 and nums[r] == 0:
            r -= 1
        elif nums[l] != 0 and nums[r] != 0:
            l += 1
    return l 
    # for i in range(len(nums)):
    #      if nums[i] == 0:
    #           res += 1
    # return res 

# O(n)
# O(1)

[ 1, 0, 2, 0, 0, 3, 4 ] l=1, r= 6[ 1, 4, 2, 0, 0, 3, 0 ] l=3,r=5[ 1, 4, 2, 3, 0, 0, 0 ] l = r= 4

[1]

[0]


def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# Your previous Plain Text content is preserved below:

# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.

# Enjoy your interview!

"""
You are given an array of integers. Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements. The algorithm should operate in place, i.e. shouldn't create a new array. The order of the nonzero elements does not matter. The numbers that remain in the right portion of the array can be anything. Example: given the array [ 1, 0, 2, 0, 0, 3, 4 ], a possible answer is [ 4, 1, 3, 2, ?, ?, ? ], 4 non-zero elements, where "?" can be any number. Code should have good complexity and minimize the number of writes to the array.
""""

[ 1, 4, 2, 3, 0, 0, 0 ]
              l  r


def swap(nums):
    # edge
    if len(nums) == 1 and nums[0] != 0: return 1
    if len(nums) == 1 and nums[0] == 0: return 0
    if not nums: return 0

    l, r = 0, len(nums)-1 # 0, 6
    while l +1 <= r:
        if nums[l] != 0 and nums[r] == 0:
            pass
        elif nums[r] == 0 and nums[r] != 0:
            # swap
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        elif nums[l] == 0 and nums[r] == 0:
            r -= 1
        elif nums[l] != 0 and nums[r] != 0:
            l += 1
    if nums[r] == 0: return l
    elif nums[l] == 1: return r
    return max(l, r)


# O(n)
# O(1)

[ 1, 0, 2, 0, 0, 3, 4 ] l=1, r= 6[ 1, 4, 2, 0, 0, 3, 0 ] l=3,r=5[ 1, 4, 2, 3, 0, 0, 0 ] l = r= 4

[1]

[0]


[1,1,1,1] l=3,r=3

[0,0,0]


""""
The Facebook company store sells stickers that say the word “facebook” on them. We just got a new shipment in, and we have way more than we know what to do with. We came up with a plan: we can make posters by cutting and pasting the letters in the word "facebook" to make other words. 
Given a particular source string representing a word on a sticker, write a function that tells me how many stickers of that string I need in order to make a given target string. Your function should take in both a source string and target string, and return the number of stickers.

Examples
source == "facebook", target == "fee": return 2
source == "facebook", target == "BOO": return 1
source == "facebook", target == "coffee kebab": return 3
"""


""""
The Facebook company store sells stickers that say the word “facebook” on them. We just got a new shipment in, and we have way more than we know what to do with. We came up with a plan: we can make posters by cutting and pasting the letters in the word "facebook" to make other words. 
Given a particular source string representing a word on a sticker, write a function that tells me how many stickers of that string I need in order to make a given target string. Your function should take in both a source string and target string, and return the number of stickers.

Examples
source == "facebook", target == "fee": return 2
source == "facebook", target == "BOO": return 1
source == "facebook", target == "coffee kebab": return 3
"""

th = {f:1, e:2}
sh = {f:1, a:1, c:1, e:1, b:1, o:2, k:1}  O(n+m)
O(m)
from collections import defaultdict
def find_count(source, target):
    th, sh = defaultdict(int), defaultdict(int)
    for ele in source:
        sh[ele] += 1
    for e in target:
        th[e] += 1
     
    # count = 0
    res = []
    for k, v in th.items():
        if k in sh:
            if v >= sh[k]:
                if v%sh[k]: res.append(int(v//sh[k] + 1))
                else: res.append(int(v/sh[k]))
        if k not in sh:
            return 0
    return max(res)


source == "facebook", target == "coffee kebab": return 3

th = {f:2, e:3, o: 1, b:2, a:1}
sh = {f:1, a:1, c:1, e:1, b:1, o:2, k:1}  O(n+m)