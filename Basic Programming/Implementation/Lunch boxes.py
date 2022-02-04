def lunch_box(boxes,need):
    temp = 0
    count=0
    for x in need:
        temp+=x
        if temp<=boxes:
            count+=1
        else:
            break
    return count

T = int(input())
for x in range(T):
    LunchSchool = list(map(int,input().split()))
    S = sorted(list(map(int,input().split())))
    ans = lunch_box(LunchSchool[0],S)
    print(ans)