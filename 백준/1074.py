import sys
input = sys.stdin.readline

n, r, c = map(int, input().split()) #2, 3, 1

start_point = [(0,0), (0, 2**n), (2**n, 2**n)]

def zigzag(start, size, sum_plus, init_sum):
    if size == 0:
        return

    start_point = [
                    (start[0], start[1]),
                    (start[0], start[1] + (2 ** (size-1))),
                    (start[0] + (2 ** (size-1)), start[1]),
                    (start[0] + (2 ** (size-1)), start[1] + (2 ** (size-1)))
                   ]
    sum = init_sum # 0, 4, 8, 12
    for i in start_point:
        if i[0] == r and i[1] == c:
            print(sum)
            exit()
        zigzag(i, size-1, sum_plus//4, sum)
        sum+=sum_plus
    return

zigzag([0,0], n, 4**(n-1), 0)