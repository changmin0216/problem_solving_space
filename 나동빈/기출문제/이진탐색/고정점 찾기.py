import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1

def binary_search(arr, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1
print(binary_search(arr, left, right))