import sys
input = sys.stdin.readline
from collections import deque

s = list(input())
tag = False
q = deque()
result = ''
for v in s:
    if not tag:
        if v == '\n' or v == ' ':
            while q:
                result += q.pop()
            result += ' '

        else:
            if v == '<':
                while q:
                    result += q.pop()
                tag = True
            q.append(v)
    else:
        q.append(v)
        if v == '>':
            while q:
                result += q.popleft()
            tag = False
print(result)