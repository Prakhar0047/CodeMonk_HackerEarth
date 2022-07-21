def toggle(st):
    final=''
    for x in st:
        if x.isupper() == True:
            temp=x.lower()
            final+=temp
        else:
            temp=x.upper()
            final+=temp
    return final

s = input()
ans = toggle(s)
print(ans)