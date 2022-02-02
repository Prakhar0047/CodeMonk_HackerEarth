"""
What is the minimum cost you have to pay for ballons.
GP = Green Purple
"""

def cost(col1, col2, green, purple):
    return min(((green*col1)+(purple*col2)),((green*col2)+(purple*col1)))

T = int(input())
for x in range(T):
    c1,c2 = 0,0
    GP = list(map(int, input().split()))
    N = int(input())
    for y in range(N):
      c1c2 = list(map(int,input().split()))
      c1+=c1c2[0]
      c2+=c1c2[1]
    ans = cost(c1,c2,GP[0],GP[1])
    print(ans)