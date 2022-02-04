def special(num):

    f = num

    while True:
        st=[]    
        st.extend(str(f))
        n = list(map(int,st))
        if sum(n)%4==0:
            return f
        else:
            f+=1

T = int(input())
for x in range(T):
    temp = int(input())
    ans = special(temp)
    print(ans)