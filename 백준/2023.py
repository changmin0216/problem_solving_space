import sys
import math
input = sys.stdin.readline

# n = int(input())

def check_prime(num):
    if num==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def dfs(depth):
    if depth == n:
        print(''.join(map(str, result)))
        return
    for i in range(1, 10):
        result.append(i)
        if check_prime(int(''.join(map(str, result)))):
            dfs(depth+1)
        result.pop()

    return

n = int(input())
result = []

dfs(0)