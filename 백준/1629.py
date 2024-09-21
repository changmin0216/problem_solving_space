import sys
input = sys.stdin.readline

a,b,c = map(int,sys.stdin.readline().split())

def multi(a, b, c):
    if b==1:
        return a%c
    else:
        tmp = multi(a, b//2, c)
        if b%2==0:
            return tmp * tmp % c
        else:
            return tmp * (tmp * a) % c

print(multi(a,b,c))


# print(pow(a, b, mod=c))