k=int(input().split()[1])
c=0
m=[0]*k
for i in input().split():
    m[int(i)%k]+=1
for i in m:
    c+=i*(i-1)
print(c)