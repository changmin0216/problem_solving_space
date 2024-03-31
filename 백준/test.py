from collections import deque

q = deque([(2, 3)])
a, b = q.popleft()
print(a, b)