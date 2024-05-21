import sys
import re
input = sys.stdin.readline

s = input().rstrip()

s_list = []
sum = 0
for i in range(len(s)):
    if s[i].isdigit():
        sum += int(s[i])
    else:
        s_list.append(s[i])
s_list.sort()

print(''.join(map(str, s_list)), end='')
print(sum)
