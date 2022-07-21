def pic(width, height, req):
    if width>=req and height>=req:
        if width == height:
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")

L = int(input())
N = int(input())
for x in range(N):
    WH = list(map(int,input().split()))
    pic(WH[0], WH[1], L)