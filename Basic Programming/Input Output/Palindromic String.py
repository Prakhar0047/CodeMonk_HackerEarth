def palindrom(st):
    if st == st[::-1]:
        print("YES")
    else:
        print("NO")
        
x = input()
palindrom(x)