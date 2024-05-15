import sys
input = sys.stdin.readline

# n = int(input())
#
# h, m, s = 0, 0, 0
#
# cnt = 0
# while(1):
#     s+=1
#     if (s==60):
#         s = 0
#         m+=1
#         if(m==60):
#             m = 0
#             h+=1
#     if h%10 == 3 or m%10==3 or m//10==3 or s%10==3 or s//10==3:
#         cnt+=1
#     if h==n and m == 59 and s == 59:
#         break
# print(cnt)

def main():
    n = int(input())

    cnt = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                time = str(i) + str(j) + str(k)
                if '3' in time:
                    cnt+=1
    print(cnt)

if __name__ == "__main__":
    main()