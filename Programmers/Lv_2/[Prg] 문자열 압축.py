# 풀이 1 (240110) : 성공
def solution(s):
    """
    모든 경우의 수를 직접 구현함 
    (문자열 최대 길이 1000이므로 괜찮음)
    """
    n = len(s)
    answer = n
    
    for split_n in range(1, n//2+1): # split_n : 문자열 절반 끼리 분리 가능
        compressed = ""
        prev = ""
        cnt = 1
        # split_n개 단위로 문자를 자르고, 압축 문자열 생성
        for i in range(0, n, split_n): 
            if prev and prev == s[i : min(i+split_n, n)]:
                cnt += 1 
            else:
                compressed += str(cnt) + prev if cnt != 1 else prev 
                prev = s[i : min(i+split_n, n)]
                cnt = 1
        if cnt != 1:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
        
    return answer
