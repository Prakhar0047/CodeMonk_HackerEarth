def anti(st):
    l = []
    l.extend(st)
    if l == l[::-1]:
        return -1
    else:
        a = sorted(l)
        b = ''.join(a)
        return b

T = int(input())
for x in range(T):
    temp = input()
    ans = anti(temp)
    print(ans)