from collections import deque

q = deque()
q.append((0,0))
y, x = q.popleft()
print(y, x)