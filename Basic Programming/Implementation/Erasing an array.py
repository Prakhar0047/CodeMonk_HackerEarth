# i==x-1,,j==x

def erase(li):
    ope = 1
    so = sorted(li)
    if li == so:
        print(1)
    else:
        for x in range(1,len(li)):
            if li[x-1]> li[x]:
                ope+=1
        print(ope) 

T = int(input())
for x in range(T):
    e = int(input())
    elements = list(map(int,input().split()))
    erase(elements)