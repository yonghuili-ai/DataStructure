class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = {}
        n = len(s)
        res = [[] for _ in range(n)] # must use this, which create different empty [] at each index
        # if using [[]]*n then all the inner [] is the same and will lead to wrong solution!
        # print(res)
        for idx, char in enumerate(order):
            h[char] = idx
        # print("h: ", h)


        for idx, char in enumerate(s):
            if char in h:
                res[h[char]].append(char)
            else:
                res[-1].append(char)

        final_res = []
        for sublist in res:
            for ele in sublist:
                final_res.append(ele)
        return ''.join(final_res)
