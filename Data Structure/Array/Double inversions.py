def invert(normal,reverse):
    pass

T = int(input())
for x in range(T):
    ele = int(input())
    a = list(map(int,input()))
    r = list(map(int,input()))
    ans = invert(a,r)
    print(ans)