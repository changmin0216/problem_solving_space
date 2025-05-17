for case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):

        max_index = arr.index(max(arr))
        min_index = arr.index(min(arr))

        arr[max_index]-=1
        arr[min_index]+=1

    result = max(arr)-min(arr)

    print(f'#{case} {result}')