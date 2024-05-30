# encoding: utf-8

# input = 'bytedance hello world'
# output ='world hello bytedance'

# input = 'bytedance helloo world '
# output ='world helloo bytedance'

# input = 'bytedance  helloo    world     abc'
# output = 'abc world helloo bytedance'

# Requirement: time O(n), space O(1)

def reverse_str(s):
    s_list = list(s.strip())
    
    def reverse(lst, l, r):
        while l < r and l >=0 and r < len(lst):
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        

    reverse(s_list, 0, len(s_list)-1)

    start = 0
    for end in range(len(s_list)):
        if s_list[end] == ' ':
            reverse(s_list, start, end-1)
            start = end + 1
    reverse(s_list, start, len(s_list)-1)

    return ' '.join(s_list)

s = "bytedance hello world"
print(reverse_str(s))

s1 = "bytedance hello world "
print(reverse_str(s1))


s2 = "bytedance helloo world here"
print(reverse_str(s2))