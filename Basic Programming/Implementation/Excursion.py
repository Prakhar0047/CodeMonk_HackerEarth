def rooms(boys, girls, seat):
    room_boys,room_girls=0,0
    
    room_boys = boys//seat
    if boys%seat == 0:
        pass
    else:
        room_boys+=1
    
    room_girls = girls//seat
    if girls%seat == 0:
        pass
    else:
        room_girls+=1
    return room_girls+room_boys


T = int(input())
for x in range(T):
    NMK = list(map(int,input().split()))
    ans = rooms(NMK[0],NMK[1],NMK[2])
    print(ans)