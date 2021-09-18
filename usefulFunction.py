#2차원 리스트 90도 회전 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이
    m = len(a[0]) #열 길이
    result = [[0]*n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n-1-r] = a[r][c]
    return result
