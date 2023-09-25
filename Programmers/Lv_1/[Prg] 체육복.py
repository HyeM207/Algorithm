## 문제 - lv.1
'''
# #1-230413 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : reserve를 딕셔너리화 한 후, 여벌이 도난 경우 처리 후, 옷 분실자에게 줄 수 있는 지 확인한다.
'''
def solution(n, lost, reserve):
    answer = 0
    reserv_dict = {}
    
    for r in reserve : 
        reserv_dict[r] = reserv_dict.get(r,0) + 1
    
    # 여벌가져온 학생이 도난당한 경우 제외 
    for l in lost : 
        if reserv_dict.get(l) :
            reserv_dict[l] = -1
    
    for l in lost  :
        if reserv_dict.get(l) :
            pass
        elif reserv_dict.get(l-1,0) > 0 :
            reserv_dict[l-1] -= 1
        elif reserv_dict.get(l+1,0) > 0 :
            reserv_dict[l+1] -= 1
        else : 
            answer += 1
    return n-answer

'''
# #2-230413 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : (강의 참고) 학생 n명에 대한 n+2 리스트를 만들어서 옷을 관리함
'''
def solution(n, lost, reserve):
    std = [1] * (n+2)
    
    for r in reserve : 
        std[r] += 1
        
    for l in lost : 
        std[l] -=1
    
    for i in range(1, n+1) : 
        # 핵심 로직
        if std[i-1] == 0 and std[i] == 2 :
            std[i-1:i+1] = [1,1]
        elif std[i+1] == 0 and std[i] == 2 :
            std[i:i+2] = [1,1]
             
    return len([ x for x in std[1:n+1] if x>0])

'''
# #3-230413 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : (강의 참고) set으로 집합화하여 '여벌학생이 분실'한 경우를 제외하고, 여벌 집합을 for문을 돌며 잃어버린 학생들에게 나눠준다.
'''
def solution(n, lost, reserve):
    s= set(lost) & set(reserve) # 교집합
    l = set(lost) - s
    r = set(reserve) - s
    
    for x in sorted(r) :
        if x-1 in l : 
            l.remove(x-1)
        elif x+1 in l :
            l.remove(x+1)
                
    return n - len(l)