##= 문제 - lv.2
'''
# #1-230418 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 이전의 프로세스 배포에 필요한 작업 일수를 due변수에 저장하고 현재 프로세스에 필요한 작업일수 workdays를 계산하여,
        이전 프로세스 배포 기간에 포함되면 cnt+=1 아니면 그 다음 배포일자로 due를 교체하고, 전단계의 배포할 프로세스 수를 answer에 append한다.  
        난이도는 lv1에 가까움
'''
import math
def solution(progresses, speeds):
    answer = [] 
    due = -1 # 앞 프로세스의 배포에 필요한 작업일수
    cnt = 0
    
    for i in range(len(progresses)):
        workdays = math.ceil((100-progresses[i])/speeds[i]) # 필요한 작업 일수 계산
        
        if due == -1 : # 첫번째 프로세스 작업을 위한 예외 적용
            due = math.ceil((100-progresses[0])/speeds[0])
            cnt += 1
        elif workdays > due : 
            answer.append(cnt)
            due = workdays
            cnt = 1
        else :  # 앞 프로세스의 배포 기간안에 포함되면 배포 개수 += 1
            cnt += 1
    
    answer.append(cnt)
    
    return answer