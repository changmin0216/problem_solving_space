import sys
input = sys.stdin.readline

zero = []
ary = []

for i in range(9):
    tmp = list(map(int, input().rstrip()))
    for j in range(9):
        if tmp[j]==0:
            zero.append((i, j))
    ary.append(tmp)

def check_row(num, y):
    for i in range(9):
        if num==ary[y][i]:
            return False
    return True

def check_col(num, x):
    for i in range(9):
        if num==ary[i][x]:
            return False
    return True

def check_three(num, y, x):
    cy = (y//3)*3
    cx = (x//3)*3

    for i in range(3):
        for j in range(3):
            if ary[cy+i][cx+j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            for j in range(9):
                print(ary[i][j], end='')
            print()
        exit()

    ey, ex = zero[depth]

    for i in range(1, 10):
        if check_col(i, ex) and check_row(i, ey) and check_three(i, ey, ex):
            ary[ey][ex] = i
            dfs(depth+1)
            ary[ey][ex] = 0

dfs(0)