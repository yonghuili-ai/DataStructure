import math 
def encryption(s):
    # Write your code here
    if len(s) == 1: return s
    s.replace(' ', '')
    n = len(s)
    row, col = int(math.sqrt(n)), math.ceil(math.sqrt(n))
    # do not miss the example case chillout, Rewritten with 3 columns and 3 rows (2*3=6<8 so we have to use 3 row.)
    # print(row, col)
    if row * col < n: row += 1
    mat = [[None for _ in range(col)] for _ in range(row)]
    # print(mat)
    for idx, char in enumerate(s):
        # print(idx, char)
        # print(idx//col, idx%col)
        mat[idx//col][idx%col] = char

    word = ''
    for j in range(col):
        for i in range(row):
            if not mat[i][j]: continue
            word = word + mat[i][j]
        word = word + " "
    return word

print(encryption('chillout'))