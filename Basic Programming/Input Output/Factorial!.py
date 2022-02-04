def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1)

N = int(input())
ans = fact(N)
print(ans)