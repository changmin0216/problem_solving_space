from collections import defaultdict
def solution(s):
    answer = []
    dict_ = defaultdict(int)
    set_ = set()
    for i in range(len(s)):
        if s[i] in set_: #만약 앞에 있어
            answer.append(i-dict_[s[i]])
            dict_[s[i]] = i
        else:
            set_.add(s[i])
            dict_[s[i]] = i
            answer.append(-1)
    return answer

print(solution("foobar"))