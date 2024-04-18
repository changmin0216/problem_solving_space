import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()

first = ary[-1]
second = ary[-2]

cnt = int(m/(k+1))*k
cnt += m % (k+1)

result = 0
result += cnt*first
result += (m-cnt)*second

print(result)