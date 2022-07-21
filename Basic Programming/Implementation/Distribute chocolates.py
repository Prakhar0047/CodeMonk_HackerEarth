"""
def chocolate(choc,stu):
    temp = 0
    while choc>stu:
        temp+=1
        choc-=temp
        if choc<stu:
            return choc

T = int(input())
for x in range(T):
    c,n = input().split()
    ans = chocolate(int(c),int(n))
    print(ans)
"""

T = int(input())

for i in range(T):

    c,s=map(int,input().split())

    total_cnt=(s*(s+1))//2 # Here i am distributing 1,2,3....n chocolates initially 

    if (s*(s+1))//2>c: # Checking if initial distribution exceeds chocolate limit

        print(c)

    else:

        remaining=c-total_cnt # Remaining chocolates after initial distribution

    print(remaining%s) # We can get the remaining no. of chocolates like this, because we are going to add 1 chocolate to each student every time
