import sys
input = sys.stdin.readline

n, b = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def multi_matrix(a, b):
    x = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j] += a[i][k]*b[k][j]
            x[i][j]%=1000

    return x

def square(a, b):
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j]%=1000
        return a

    tmp = square(a, b//2)
    if b%2==1:
        return multi_matrix(multi_matrix(tmp, tmp), a)
    else:
        return multi_matrix(tmp, tmp)

result = square(matrix, b)

for i in result:
    print(*i)