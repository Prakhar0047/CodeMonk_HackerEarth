# Have someproblem in question it self.

def prime(x=0, y=100000):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

def f(i,j):
    n = i+j
    count=0
    for x in prime_divisor:
        if n%x == 0:
            count+=1
    return count

def spe(row, column):
    final = 0
    for i in range(1,row+1):
        for j in range(1,column+1):
            final+=f(i,j)
    return final

T = int(input())
prime_divisor = prime()
for x in range(T):
    NM = list(map(int,input().split()))
    ans = spe(NM[0],NM[1])
    print(ans)