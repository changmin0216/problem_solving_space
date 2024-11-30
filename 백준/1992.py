import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
def recur(y, x, n):
    tmp = graph[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j]!=tmp:
                tmp = -1
                break
        else: #break 안했으면
            continue
        break

    if tmp == -1:
        n = n//2

        print('(', end='')
        recur(y, x, n)
        recur(y, x+n, n)
        recur(y+n, x, n)
        recur(y+n, x+n, n)
        print(')', end='')
    else:
        print(tmp, end='')

recur(0, 0, n)