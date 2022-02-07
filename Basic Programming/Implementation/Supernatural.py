    def superNatural(i):
        product = 1
        count = 0
        for x in range(1,101):
            while (x != 0):
                product = product * (i % 10)
                i = i // 10
            if product == i:
                count+=1
        return count

    n = int(input())
    ans = superNatural(n)
    print(n)