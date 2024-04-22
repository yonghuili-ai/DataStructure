# typical question using merge sort
# time O(nlogn) -- logn level, n element for each element merge
# space O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.dfs(nums)
    
    def dfs(self, lst):
        if len(lst) == 1:
            return lst
        mid = len(lst)//2
        l1 = self.dfs(lst[:mid])
        l2 = self.dfs(lst[mid:])
        return self.merge(l1, l2)
        
        
        
    def merge(self, l1, l2):
        p1, p2 = 0, 0 
        res = []
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                res.append(l1[p1])
                p1 += 1
            else:
                res.append(l2[p2])
                p2 += 1
        res.extend(l1[p1:])
        res.extend(l2[p2:])
        return res