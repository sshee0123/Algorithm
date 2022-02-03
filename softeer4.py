import sys
import bisect
n = int(sys.stdin.readline())
rocks = list(map(int,sys.stdin.readline().split()))

answer = []
answer_rev = []
target = [1]*n
target_rev = [1]*n

for i in range(n):
    if len(answer) == 0:
        answer.append(rocks[i])
    else:
        if rocks[i]>answer[-1]:
            answer.append(rocks[i])
        else:
            index = bisect.bisect_left(answer,rocks[i])
            answer[index] = rocks[i]

    if len(answer_rev) == 0:
        answer_rev.append(rocks[n-i-1])
    else:
        if rocks[n-i-1]>answer_rev[-1]:
            answer_rev.append(rocks[n-i-1])
        else:
            index = bisect.bisect_left(answer_rev,rocks[n-i-1])
            answer_rev[index] = rocks[n-i-1]
    
    target[i] = len(answer)
    target_rev[n-i-1] = len(answer_rev)

sum_target = [0]*n

for i in range(n):
    sum_target[i] = target[i]+target_rev[i]
print(max(sum_target)-1)    
