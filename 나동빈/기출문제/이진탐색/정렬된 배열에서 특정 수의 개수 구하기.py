import sys
input = sys.stdin.readline

N, x = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = N - 1

cnt = 0

def first(array, target, start, end):
    first_index = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > x:
            end = mid - 1
        elif array[mid] < x:
            start = mid + 1
        else:
            first_index = mid
            end = mid - 1
    return first_index

def last(array, target, start, end):
    last_index = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > x:
            end = mid - 1
        elif array[mid] < x:
            start = mid + 1
        else:
            last_index = mid
            start = mid + 1
    return last_index

first_index = first(arr, x, left, right)
last_index = last(arr, x, left, right)

if first_index == -1 or last_index == -1:
    print(-1)
else:
    print(last_index - first_index + 1)