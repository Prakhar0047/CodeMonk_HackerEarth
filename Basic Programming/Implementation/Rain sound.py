def rain(l,r,s):
    co = []
    for x in range(r+1):
        temp = x*s
        if temp>=l and temp<=r:
            co.append(x)
    mi = min(co)
    ma = max(co)
    if len(co) == 0:
        return [-1,-1]
    else:
        return [mi,ma]

T = int(input())

for x in range(T):
    L,R,S = input().split()
    ans = rain(int(L),int(R),int(S))
    print(ans[0],ans[1])