from collections import defaultdict

def count_word(lst):
    d = defaultdict(int)
    for i in lst:
        d[i] += 1
    print(d)
    return d

count_word(['cat','cat','dog','snake'])