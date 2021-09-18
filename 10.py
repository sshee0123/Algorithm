#10 자물쇠와 열쇠
#2020 카카오 신입 공채

#2차원 리스트 90도 회전 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이
    m = len(a[0]) #열 길이
    result = [[0]*n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n-1-r] = a[r][c]
    return result

#합이 1인지 확인하는 함수
def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    #자물쇠의 크기를 3배로 늘이기
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    #커진 자물쇠의 가운데에 원래 자물쇠 삽입
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    #4가지 방향에 대해 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
              
                #자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                #잘 맞는지 확인
                if check(new_lock) == True:
                    return True
                  
                #자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
