def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col-1], -x[0]))

    for i in range(row_begin-1, row_end):
        sum_ = 0
        for j in range(len(data[i])):
            sum_+=(data[i][j]%(i+1))
        if i==row_begin-1:
            answer = sum_
        else:
            answer = answer^sum_

    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))