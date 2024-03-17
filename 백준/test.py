import math
prime = [True] * 1001
prime[1] = False
# 소수 list
for i in range(2, int(math.sqrt(1000000))+1):
    if prime[i]:
        j=2
        while i*j<=1000000:
            prime[i*j] = False
            j+=1
