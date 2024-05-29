import sys
input = sys.stdin.readline

com = list(map(str, input().split()))

if com[0] == 'encrypt':
    l = []
    for c in com[1]:
        l.append(ord(c) - 97)


    for i in range(len(com[3])):
        l[i] = l[i] + (ord(com[3][i]) - 97)
        if l[i] > 25:
            l[i]-=26


    if int(com[2])<0:
        t = abs(int(com[2]))%len(com[1])

        temp = l[-t:]
        temp += l[:-t]
    else:
        t = int(com[2])%len(com[1])
        temp = l[t:]
        temp = temp + l[:t]

    for v in temp:
        print(chr(v+97), end='')

else:
    l = []
    for c in com[3]:
        l.append(ord(c) - 97)

    if int(com[2]) > 0:
        t = int(com[2]) % len(com[1])

        temp = l[-t:]
        temp += l[:-t]
    else:
        t = abs(int(com[2])) % len(com[1])
        temp = l[t:]
        temp = temp + l[:t]

    l = []
    for c in com[1]:
        l.append(ord(c) - 97)

    for i in range(len(l)):
        temp[i]-=l[i]
        if temp[i] < 0:
            temp[i]+=26


    for v in temp:
        print(chr(v+97), end='')