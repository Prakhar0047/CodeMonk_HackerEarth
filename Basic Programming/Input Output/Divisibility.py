N = int(input())
A = list(map(str,input().split()))
test = ''
for x in A:
    temp = x[-1]
    test+=temp

if int(test) % 10 == 0:
    print("Yes")
else:
    print("No")