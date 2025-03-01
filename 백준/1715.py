import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

if n==1:
    print(0)
else:
    q = []
    for i in range(n):
        heapq.heappush(q, arr[i])
    answer = 0
    while len(q)>=2:
        a = heapq.heappop(q)
        b = heapq.heappop(q)

        sum_ = a + b
        heapq.heappush(q, sum_)

        answer += sum_
    print(answer)