from collections import deque

q = deque()

q.append('I')
q.append('O')
q.append('I')

if ''.join(q)=='IOI':
    print('YES')