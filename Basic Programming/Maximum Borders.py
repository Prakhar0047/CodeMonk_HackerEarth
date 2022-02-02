def borders(row, column, borders_collection):
    count = 0
    for x in range(row):
        for y in range(column):
            if test_str[y] == "#":
                count+=1
                if test_str[y-1] == "#":
                    pass
                else:
                    break
        print(count)
        count=0

t = int(input())
bod = 0
for x in range(t):
    rc = list(map(int,input().split()))
    for x in range(rc[0]):
        row = input()
        bod.append(row)
        borders(rc[0], rc[1], bod)