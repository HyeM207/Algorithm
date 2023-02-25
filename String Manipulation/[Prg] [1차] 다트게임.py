# 문제 - lv.1
'''
# #1-230225 성공
    - 정확성: 100.0
    - 합계: 100.0 / 100.0
    - 풀이 : 문자열 자르는데 시간을 많이 썼다. while문과 idx를 이용하여 점수(숫자)에 접근하여 차례로 점수, 보너스, 옵션 계산 후 다음 점수가 있는 인덱스로 idx를 옮기는 코드를 구현하였다.
'''
def solution(dartResult):
    dart_list = []
    area_score = { "S" : 1, "D" : 2, "T" : 3}
    # 한 회차별로 리스트별로 넣어서 관리할 예정 -> 각 회차별로 점수 적용 후 총합할 예정
    # 문자열은 앞에서부터 접근하여 점수 바로바로 계산할 예정
    
    idx = 0
    while idx < len(dartResult):  
        # 1. 점수 분류
        if dartResult[idx].isdigit() :
            score = int(dartResult[idx])
            
            if dartResult[idx+1].isdigit() : # 10인지 확인   
                score = 10
                idx += 1
            
        # 2. 보너스 계산        
        score = score ** area_score[dartResult[idx+1]]
        
        # 3. 옵션 계산
        if idx+2 < len(dartResult) and dartResult[idx+2] in ("*", "#"): 
            if dartResult[idx+2] == "#" : #3-1. '#' 옵션
                score = score * (-1)
            else : #3-2. '*' 옵션
                score *= 2
                if len(dart_list) > 0 :
                    dart_list[-1] *= 2
            idx += 3
        else : #3. 옵션 없음
            idx += 2 
            
        dart_list.append(score)
    return sum(dart_list)

'''
# 더 나은 풀이(programmers 다른 사람 풀이 참고)  : 아래 풀이는 정규 표현식을 이용하여 dart를 추출 후, 바로 점수 계산하는 코드이다. 정규표현식도 기억해둬야겠다.
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
'''