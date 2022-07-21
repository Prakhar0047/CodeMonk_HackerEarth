def code(st):
    l=[]
    l.extend(st)
    flag=0
    if l[2] not in ('A','E','I','O','U','Y'):
        if (int(l[0])+int(l[1]))%2==0:
            if (int(l[3])+int(l[4]))%2==0:
                if (int(l[4])+int(l[5]))%2==0:
                    if (int(l[7])+int(l[8]))%2==0:
                        flag=1
    if flag==1:
        print("valid")
    else:
        print("invalid")

tag = input()
code(tag)