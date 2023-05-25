# 문제 - lv.2
"""
# #1-230525 성공
    풀이 : 
        skill에 있는지 확인하고,
            있다면 이전 단계를 배웠는지 확인한다.
                -> 확인 방법은 index() 확인 (skill 길이 최대 26)
"""
def solution(skillset, skill_trees):
    answer = 0
    
    for skill in skill_trees : 
        preq_idx = 0  # 배워야 할 선행스킬 인덱스 
        flag = True
        for s in skill : 
            if s in skillset :
                check = skillset.index(s)  #배우려고 하는 스킬의 선행스킬 인덱스
                # 현 단계 선행스킬을 배우면 다음단계로 +1
                if check == preq_idx :  
                    preq_idx += 1
                # 선행스킬보다 큰 스킬 배우려고하면 break
                elif check > preq_idx : 
                    flag = False
                    break
        if flag : 
            answer += 1
                
    return answer