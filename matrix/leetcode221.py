class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def check_square(i, j, sideLen):
            # print("inner loop")
            # print(i,j,sideLen)
            for x in range(i, sideLen + i): # must understand, here should be sideLen + i, use case 1 as example on (1, 2)
                for y in range(j, sideLen + j):# must understand, here should be sideLen + j
                    if matrix[x][y] != "1":
                        # print(x,y)
                        return False
            return True
            

        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        max_s = 0 
        if r == 1 and c == 1 and matrix[0][0] == 1: return 1
        if r == 1 and c == 1 and matrix[0][0] == 0: return 0
        for i in range(r):
            for j in range(c):
                # check if the current number is 1
                # 0, 1, 0
                if matrix[i][j] == "1":
                    flag = True # use to break from while loop 
                    sideLen = 1
                    while sideLen <= r - i and sideLen <= c - j and flag:
                        print(max_s)
                        flag = check_square(i, j, sideLen)
                        if flag: 
                            # print(i, j, sideLen, flag)
                            sideLen += 1
                        else: 
                            # print(i, j, sideLen, flag)
                            break
                    # print(sideLen-1, max_s)
                    max_s = max(sideLen-1, max_s)
                        # if not flag: 
                        #     print(i, j, sideLen)
                        #     max_s = max(sideLen, max_s, 1)
                        # else:

        return max_s * max_s
