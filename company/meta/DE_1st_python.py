# 1. Fill the None value with previous non None value
# [1, None, 1, 2, None] --> [1, 1, 1, 2, 2]
def fill_none(arr):
    if len(arr) <= 1: return arr
    i = 1
    while i < len(arr):
        if arr[i] is None and arr[i-1] is not None:
            arr[i] = arr[i-1]
        i += 1
    return arr 

arr1 = [1]
arr2 = [None]
arr3 = [1, None, 1, 2, None]
arr4 = [1, None, None, None, 1]

print(fill_none(arr1))
print(fill_none(arr2))
print(fill_none(arr3))
print(fill_none(arr4))


# 2. Complete a function that returns a list containing all the mismatched words(case sensitive) between two given input strings
# find_mismatch("HOW ARE you", "How are you") --> ["HOW", "ARE", "How", "are"]
# 注意这里是case sensitive，所以ARE和are不相同

def find_mismatch(s1, s2):
    set1 = set(s1.split(" "))
    set2 = set(s2.split(" "))
    return list((set1 - set2) | (set2 - set1))

print(find_mismatch("HOW ARE you", "How are you"))
print(find_mismatch("HOW 2", "How are you"))


# 3. Complete a function that returns the number of times a given character occurs in the given string
# find_occur('missisipi', 's') --> 3
# 设置一个counter，整个string扫一遍

from collections import defaultdict
def counter(s, char):
    d = defaultdict(int)
    for ele in s:
        if ele == char:
            d[char] += 1
    return d[char]

print(counter('missisipi', 's'))
print(counter('missisipi', 'b'))


# 4. Complete a function that returns the smallest key(sorted in ascending order alphabetically) of the given input dictionary containing nth hgihest value
# dictionary: {'a': 1, 'b': 2, 'c': 100, 'd': 30}, n : 2 (2nd highest value)
# output: 'd'

from collections import defaultdict
# sort dictionary using value
def n_largest(d,n):
    # corner case 
    if n == 0: return -1
    if n > len(d): return -1
    # not consider tie 
    # l = sorted(d.items(), key=lambda x:x[1], reverse=True)
    # print(l)
    # return l[n-1][0]
    # consider tie condition
    new_d = defaultdict(set)
    for k, v in d.items():
        new_d[v].add(k)
    print(new_d)
    return list(sorted(new_d.items(), key=lambda x: x[0], reverse=True)[n-1][1])

# 1 
# d.items() contains tuples, where each tuple is a key-value pair from the dictionary.
# Define a dictionary
# d = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # Use the items() method
# items = d.items()

# # Print the items view object
# print(items)  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# # Convert to a list of tuples
# items_list = list(items)
# print(items_list)  # Output: [('name', 'Alice'), ('age', 25), ('city', 'New York')]

# 2 sorted returns a new list, sorted(iterable, key=function such as len or lambda x:x[1])

print(n_largest({'a': 1, 'b': 2, 'c': 100, 'd': 30}, 2))
print(n_largest({'a': 1, 'b': 2, 'c': 100, 'd': 30}, 0))
print(n_largest({'a': 1, 'b': 2, 'c': 100, 'd': 100}, 1))

# 5. Balance the array
# Given an array with n elements provide a dictionary of all the needed elements to balance the array as keys of that dictionary and number of repeated occurraences of each of those elements that are required to balance the given array as values
# Balance array would be an array containing all elements that appear equal number of times
# For example:
# -- input array: [4, 5, 11, 5, 6, 11]
# -- output: {4: 1, 6: 1}
# -- We need 1 instance of elements 4 and 1 instance of element 6 in order to balance the given input array where each element would appear max 2 times

def balance_arr(arr):
    h, res = defaultdict(int), defaultdict(int)
    mx = 0
    for ele in arr:
        h[ele] += 1
        mx = max(mx, h[ele])
    for k, v in h.items():
        if v < mx:
            res[k] = mx - v
    return res

arr1 = [4, 5, 11, 5, 6, 11]
arr2 = [4, 5, 11, 5, 5, 6, 11]
print(balance_arr(arr1))
print(balance_arr(arr2))


# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# list(prev[0]): This attempts to convert prev[0] into a list. If prev[0] is a single value (like an integer or a string), this operation will fail or produce unexpected results.

# [prev[0]]: This creates a new list containing just the first element of prev.


# When you write prev[1:].append(prev[0]), it first creates a new list with prev[1:], and then appends prev[0] to this new list. But because append() returns None, the result assigned to new is None.
# right way is prev[1:]+ [prev[0]]

def rotLeft(a, d):
    # Write your code here
    prev = a
    while d > 0:
        new = prev[1:] + [prev[0]]
        d -= 1
        prev = new
    return new 
a = [1,2,3,4,5]
d = 4
print(rotLeft(a, d))



# Mock interview question


'''
Given an IP address as input, the task is to write a Python program to check whether the given IP Address is Valid or not without using RegEx.

What is an IP (Internet Protocol) Address? 
Every computer connected to the Internet is identified by a unique four-part string, known as its Internet Protocol (IP) address. An IP address (version 4) consists of four numbers (each between 0 and 255) separated by periods. The format of an IP address is a 32-bit numeric address written as four decimal numbers (called octets) separated by periods; each number can be written as 0 to 255 (E.g. – 0.0.0.0 to 255.255.255.255).

Examples: 

Input:  192.168.0.1
Output: Valid IP address

'''

def valid_ip(s):
    l = s.split('.')
    print(l)
    if len(l) != 4: return False 
    for ele in l:
        if int(ele) < 0 or int(ele) > 255:
            return False 
    return True 

print(valid_ip('192.168.0.1'))
print(valid_ip('192.-168.0.1'))

# https://www.geeksforgeeks.org/validate-an-ip-address-using-python-without-using-regex/

# 5min, read, ask 1-2 questions, start immediately, O(n) or O(1), linear search, dictionary
