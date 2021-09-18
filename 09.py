#09 문자열 압축
#2020 카카오 신입 공채

def solution(s):
    #문자열 길이 변경되므로 미리 변수에 저장
    answer = len(s)
   
    #1부터 완전탐색
    for i in range(1,len(s) // 2 + 1):
        compressed = ""
        count = 1
        prev = s[0:i]
        
        #i만큼씩 중복 비교
        for j in range(i, len(s), i):
            #같으면 압축+1
            if prev == s[j : j + i]:
                count += 1
                
            #다르면
            else:
                if count>=2:
                    compressed += str(count) + prev
                #1은 표시 생력
                else:
                    compressed += prev
                    
                #초기화해서 다시 i변경 후 재탐색
                prev = s[j : j + i]
                count = 1
        
        #남은 문자열
        if count>=2:
            compressed += str(count) + prev
        else:
            compressed += prev

        answer = min(answer,len(compressed))
    return answer
