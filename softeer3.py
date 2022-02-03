import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
rocks = [1]*N

for i in range(1,N):
    max_rocks = 0
    for j in range(i):
        if l[i] > l[j]:
            if max_rocks < rocks[j]:
                max_rocks = rocks[j]
    rocks[i] = max_rocks+1
print(max(rocks))
