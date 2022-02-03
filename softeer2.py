import sys
N,K = map(int,sys.stdin.readline().split())
trail = list(sys.stdin.readline())

cnt = 0
for i in range(N):
    if trail[i] == "P":
        for j in range(i-K,i+K+1):
            if 0<=j<N:
                if trail[j] == "H":
                    trail[j] = None
                    cnt+=1
                    break
                
print(cnt)
