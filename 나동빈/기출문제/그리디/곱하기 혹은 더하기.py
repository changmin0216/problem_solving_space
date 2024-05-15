import sys
input = sys.stdin.readline

ary = list(map(int, input().rstrip()))

result = 0
for i in range(len(ary)):
    if result + ary[i] > result * ary[i]:
        result+=ary[i]
    else:
        result*=ary[i]
print(result)
