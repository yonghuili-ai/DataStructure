"""
You are given a dictionary with a key-value of {string: number} where values in the dictionary could be duplicates. You are required to extract the unique values from the dictionary where the value occurred only once.

Return a list of values where they occur only once.

Note: You can return the values in any order.

Input:

dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
Output:

find_unique_values(dictionary) -> [3,4]

"""

d = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
def find_unique_value(d):
    res = set()
    visited = set()
    for k, v in d.items():
        if v in visited:
            if v in res:
                res.remove(v)
        else:
            res.add(v)
            visited.add(v)
    return list(res)

print(find_unique_value(d))

from collections import defaultdict
def find_unique_value_2(d):
    res = defaultdict(int)
    final_res = []
    for k, v in d.items():
        res[v] += 1
    for k, v in res.items():
        if v == 1:
            final_res.append(k)

    return final_res

print(find_unique_value_2(d))
