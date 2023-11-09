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

"""
# #2-231109 성공
풀이 2
"""
import math 
def solution(progresses, speeds):
    answer = []
    """
    while문으로 n만큼 순회하며 배포 순서의 프로세스보다 뒤에 것이 작으면 같이 배포함
    """
    i = 0 
    while i < len(progresses):
        due = math.ceil( (100-progresses[i]) / speeds[i] ) # 배포 순서의 프로세스 필요 일 수 
        j = i + 1
        # 뒤의 프로세스 작업 일 수 계산 
        while j < len(progresses):
            day = math.ceil( (100-progresses[j]) / speeds[j] )
            if day > due:
                break
            j += 1
        answer.append(j-i)
        i = j
    return answer
