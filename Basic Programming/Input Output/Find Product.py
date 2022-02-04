def product(num_list):
    final=1
    for x in num_list:
        final = (final*x)%(10**9+7)
    return final

N = int(input())
l = list(map(int,input().split()))
ans = product(l)
print(ans)