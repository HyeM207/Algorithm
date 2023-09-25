# 문제 - lv.2
'''
# #1-230510실패/230525실패
    (다른 풀이 참고_https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy)
    후기 : 1차땐 이해 실패, 2차땐 구현 실패 -> 결국 다른 풀이 보며 학습함
    실패 풀이 : 
        고려 사항 :
            1. 커서 위,아래 (알파벳에 대해 내림차순 접근,오름차순접근) => 구현 O
            2. 커서 왼,오 (A를 고려해서 왼쪽으로 갈지 오른쪽으로 갈지) => 구현 못함 
'''

def solution(name):
    answer = 0
    min_move = len(name) - 1 # 초기값은 한 방향으로만 커서 움직이는 것
    
    for i, char in enumerate(name):
        # 고려사항 1
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 고려사항 2
        # 다음 연속된 A나올 때까지 next 이동
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    answer += min_move
    return answer
"""
min_move : 기존 방식
2 * i + len(name) - next : 
i + 2 * (len(name) -next)] : 
"""