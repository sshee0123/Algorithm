n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = [] #방향정보

#맵 정보(사과는 1 표시)
for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1

#방향 회전 정보
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

#동, 남, 서, 북(처음에 동쪽 = 0 )
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def simulation():
    x, y = 1, 1 #뱀의 머리 위치
    direction = 0 #처음에 동쪽
    time = 0 #초
    data[x][y] = 2 #뱀이 존재하는 위치 2로 표시
    index = 0 #다음에 회전할 정보
    q = [(x,y)] #뱀이 차지하고 있는 위치 (큐 -> 꼬리가 앞 쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        #맵이 범위 안에 있고 몸통이 없는 위치라면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny] != 2:
            #사과가 없다면 머리 이동 후 꼬리 삭제
            if data[nx][ny] == 0 :
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0
            #사과가 있다면 머리 이동 후 꼬리 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 몸통에 부딪힌다면 종료
        else:
            time+=1
            break

        #머리 이동
        x, y = nx, ny
        time += 1

        #time이 회전할 시간이면 회전
        if index<1 and time == info[index][0]:
            print("before", index)
            direction = turn(direction,info[index][1])
            index+=1
            print("after", index)
    return time

print(simulation())
