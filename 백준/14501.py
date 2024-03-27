import sys
input = sys.stdin.readline

n = int(input())

t=[]
p=[]
for _ in range(n):
    t_, p_ = map(int, input().split())
    t.append(t_)
    p.append(p_)

result = 0

def recur(day, sum):
    global result
    if day==n:
        result = max(result, sum)
        return
    elif day > n:
        return
    recur(day+t[day], sum+p[day])
    recur(day+1, sum)

recur(0, 0)
print(result)