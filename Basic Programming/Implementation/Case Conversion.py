def caseConversion (s):
    temp = ""
    flag = True
    for x in s:
        if x.isupper() == True:
            l = x.lower()
            if s[0] == x and flag == True:
                temp+=l
                flag = False
            else:
                temp+="_"
                temp+=l
        else:
            temp+=x
    return temp

T = int(input())
for _ in range(T):
    s = input()

    out_ = caseConversion(s)
    print (out_)