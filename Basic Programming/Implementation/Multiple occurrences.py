def occur(element):
    fi = 0
    s = set(element)
    print(s)
    for x in s:
        if element.count(x) == 1:
            pass
        else:
            f_res = element.index(x)

            reversed_list = element[::-1]
            first_index_in_reversed = reversed_list.index(x)
            l_res = len(element) -1 - first_index_in_reversed
            
            temp = l_res-f_res

            fi+=temp
    
    return fi

T = int(input())
for x in range(T):
    N = int(input())
    ele = list(map(str,input().split()))
    ans = occur(ele)
    print(ans)