from itertools import combinations

n,m = map(int,input().split())
house,chicken = [],[]

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1: #집일때
            house.append((r,c))
        elif data[c] == 2: #치킨집일때
            chicken.append((r,c))
#치킨집 조합
combs = list(combinations(chicken,m))

def d_sum(comb):
    result = 0
    #모든 집~치킨집 거리 구하기
    for hx,hy in house:
      #최소값 구하기
        temp = 1e9
        for cx,cy in comb:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

result = 1e9
for comb in combs:
    result = min(result,d_sum(comb))
print(result)
