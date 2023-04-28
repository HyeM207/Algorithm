# 문제 - lv.2
'''
# #1-230428 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : deque로 바꿔서 d1, d2 둘 중 합이 큰 쪽을 popleft하여 append함
    시도1(실패) - 시간 초과 (원인 2**len(deque1로 설정함) 다시 계산해보니 *4가 최대 횟수인걸 알아차리고 고침)
    개선사항 : 더 효율적으로 코드를 구현을 방법은 없는지 생각해보기 
        - 현재 테스트 케이스 상태가 불완전한거 같다. 이후에 테케 추가되면 다시 봐보면 좋을듯
'''
from collections import deque

def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    sum_q1 = sum(queue1) 
    sum_q2 = sum(queue2)
    answer = -1
    cnt = 0
    
    while True :
        if sum_q1 == sum_q2 : 
            answer = cnt 
            break
        if len(deque1) ==0 or len(deque2) ==0 or cnt >= 4*len(queue1):
            break
        if sum_q1 > sum_q2 : 
            added = deque1.popleft()
            deque2.append(added)
            sum_q1 -= added
            sum_q2 += added
        else: 
            added = deque2.popleft()
            deque1.append(added)
            sum_q2 -= added
            sum_q1 += added
        cnt += 1
        
    return answer
