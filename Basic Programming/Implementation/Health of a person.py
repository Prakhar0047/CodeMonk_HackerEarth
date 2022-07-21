T = int(input())

for x in range(T):
    num_ppl,my_walk = input().split()
    p = list(map(int,input().split()))
    w = list(map(int,input().split()))
    ppl = [0]+p
    walk = [0]+w
    sick = [0]*(int(num_ppl)+1)
    for i in range(1,int(my_walk)+1):
        for j in range(1,int(num_ppl)+1):
            if j%i == 0:
                temp = ppl[j]-walk[i]
                if temp <=0:
                    sick[j] = i
                else:
                    sick[j] = -1
    for x in range(1,len(sick)):
        print(sick[x])