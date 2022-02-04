"""
N,K = int(input().split())
stu = list(map(int,input().split()))
strength = []
for x in stu:
    strength.append(x%K)
so_sen = sorted(strength)
s = set(strength)
temp = 0
for x in s:
    a = so_sen.count(x)
    temp+=(a*(a-1))
print(temp)
"""

k=int(input().split()[1])
c=0
m=[0]*k
for i in input().split():
    m[int(i)%k]+=1
for i in m:
    c+=i*(i-1)
print(c)