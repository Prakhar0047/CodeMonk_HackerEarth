from itertools import count


def cal(start,finish,divisor):
    count=0
    for x in range(start,finish+1):
        if x%divisor==0:
            count+=1
    return count
LRK = list(map(int,input().split()))
ans = cal(LRK[0],LRK[1],LRK[2])
print(ans)