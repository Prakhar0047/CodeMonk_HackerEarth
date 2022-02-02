def zoos(str):
    z = float(str.count('z'))
    o = str.count('o')
    if o/2 == z:
        return "Yes"
    else:
        return "No"

i = input()
ans = zoos(i)
print(ans)