"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

# Need to understand several concepts through this question:
# 1. python collections class defaultdict
# https://docs.python.org/3/library/collections.html#collections.defaultdict
# defaultdict	https://docs.python.org/3/library/collections.html#collections.defaultdict	
# d = defaultdict(list)	d[k].append(value)	
# 	sorted(d.items(), lambda x:x[1])	

# 2. dictionary.items() to get all the key-value pair from dictionary in dict views, need to add list to return a list

# 3. sorted() returns a sorted list of the specified iterable object, need to join ''.join(list) to get a new word
from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for word in strs: 
        new = ''.join(sorted(word))
        d[new].append(word)
    print(d.items())
    print(d.values())
    print(list(d.values()))
    return list(d.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"])

       