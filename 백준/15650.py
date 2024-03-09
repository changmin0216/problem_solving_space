import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rs = []
chk = [False] * (n+1)

def recur(start):
    if len(rs)==m:
        print(' '.join(map(str, rs))) #print(*rs) --> rs 리스트의 각 요소를 언패킹
        return
    for i in range(start, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(i)
            chk[i] = False
            rs.pop()

recur(1)