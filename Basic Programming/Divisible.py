def solve (A):
    l = len(A)
    
    first_half = A[:l//2]
    second_half = A[(l//2):]
    
    fnum= ''
    lnum=''

    for x in first_half:
        fnum+=x[0]          

    for x in second_half:
        lnum+=x[-1]

    temp = fnum+lnum
    if int(temp)%11==0:
        print("OUI")
    else:
        print("NON")

N = int(input())
A = list(map(str, input().split()))

out_ = solve(A)