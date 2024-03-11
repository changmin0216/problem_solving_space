import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sentence = list(map(str, input().split()))
    for word in sentence:
        print(''.join(reversed(word)), end=' ') #reversed() 함수는 문자열을 뒤집은 순회 가능한 객체를 반환