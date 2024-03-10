import sys
from collections import deque

q = deque((2, 3))
x, y = q.popleft()
print(x)
