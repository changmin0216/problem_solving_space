def play(arr):


    array = [[10],[30],[50],[80]]

    score = {'A': 0,'B': 0,'C': 0}
    ass = {0: 'A', 1: 'B', 2:'C'}
    for i in range(0, len(arr), 3):
        tmp = arr[i:i+3]

        sorted_index = sorted(range(len(tmp)), key=lambda index_: arr[index_])

        for x in sorted_index:

            compare_minus = 100
            index__ = -1
            last_num = 0
            for j in range(4):
                if len(array[j]) == 0:
                    continue

                if abs(array[j][-1] - tmp[x]) < compare_minus:
                    compare_minus = abs(array[j][-1] - tmp[x])
                    index__ = j
                    last_num = array[j][-1]
                elif abs(array[j][-1] - tmp[x]) == compare_minus:
                    if last_num < array[j][-1]:
                        last_num = array[j][-1]
                        index__ = j


            if last_num > tmp[x]:
                array[index__].append(tmp[x])
            else:
                score[ass[x]]+=len(array[index__])
                array[index__] = []

        cnt = 0
        for q in range(4):
            if len(array[q]) == 0:
                cnt+=1

        if cnt == 4:
            break
    print(score)
play([55,8,29,13,7,61])