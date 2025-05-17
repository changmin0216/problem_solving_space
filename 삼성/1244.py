def dfs(num : str, n : int) -> None:
    global answer
    if n==0:
        answer = max(answer, int(num))
        return

    if (int(num), n) in set_:
        return
    set_.add((int(num), n))
    num_list = list(num)
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            dfs(''.join(num_list), n-1)
            num_list[j], num_list[i] = num_list[i], num_list[j]

############################
### 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.
t = int(input())

for i in range(t):
    num, cnt = map(str, input().split())

    answer = -1
    set_ = set()
    dfs(num, int(cnt))
    print(f'#{i+1} {answer}')