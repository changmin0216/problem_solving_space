import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ary_a = list(map(int, input().split()))
ary_b = list(map(int, input().split()))

# for _ in range(k):
#     min_a = min(ary_a)
#     max_b = max(ary_b)
#     if max_b - min_a > 0:
#         ary_b.remove(max_b)
#         ary_a.remove(min_a)
#
#         ary_b.append(min_a)
#         ary_a.append(max_b)
#     else:
#         break
# print(sum(ary_a))

ary_a.sort()
ary_b.sort(reverse=True)

for i in range(k):
    if ary_a[i] < ary_b[i]:
        ary_a[i], ary_b[i] = ary_b[i], ary_a[i],
    else:
        break
print(sum(ary_a))