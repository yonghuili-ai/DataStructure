# Pascal's Triangle 119. Pascal's Triangle II
#    1
#   1  1
# 1   2   1    
#1  3   3   1
# convert the problem into i-row, j-column
# 1
# 1  1
# 1  2  1
# 1  3  3  1

# f(i,j) = f(i-1,j-1) + f(i-1,j)
def triangle(n):
    j = 1
    res = []
    def dfs(n, j):
        if j == 1 or j == n:
            return 1
        return dfs(n-1,j-1) + dfs(n-1,j)
    while j <= n:
        res.append(dfs(n,j))
        j += 1

    return res
