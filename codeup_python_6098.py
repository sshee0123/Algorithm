arr = [[]*10 for _ in range(10)]
for i in range(10):
    arr[i] = list(map(int,input().split()))
    
x,y = 1,1
arr[x][y] = 9
while True:
    if arr[x][y]==2:
        arr[x][y]=9
        break
    
    if arr[x][y+1] !=1:
        arr[x][y]=9
        y+=1
    else:
        #아래이동
        if arr[x+1][y]!=1:
            arr[x][y]=9
            x+=1
        else:
            arr[x][y]=9
            break
        
for i in range(10):
    for j in range(10):
        print(arr[i][j],end=' ')
    print()    
            
