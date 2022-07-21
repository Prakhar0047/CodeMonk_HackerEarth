# 10^9+7
from math import factorial

N,M = input().split()
if int(N) == int(M):
    ans = factorial(int(M))
    print(ans%((10**9)+7))
else:
    temp = int(M)-int(N)
    ans = temp*factorial(int(M))
    print(ans%((10**9)+7))