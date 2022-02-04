def borders(row,borders_collection):
    for x in range(row):
        a = borders_collection[x].count("#")
        print(a)

t = int(input())
bod = []
for x in range(t):
    rc = list(map(int,input().split()))
    for x in range(rc[0]):
        row = input()
        bod.append(row)
        ans=borders(rc[0],bod)
    print(ans)