# 풀이 1 (240123) : 성공
def solution(gems):
    """
    보석 종류를 알 수 없고, 모두 순회해야지만 알 수 있음
    그렇다면 한 번만 순회하여, 가장 짧은 구간을 찾자 => left, right 포인터를 이용해서 찾아보자

    [left + 1 하는 경우]
        - left가 이미 있을때
    [right + 1 하는 경우]
        - 그 외
    """
    answer = []
    left, right = 0, 0
    types_nums = len(set(gems))
    elements = {gems[left]: 1}
    
    while left <= right and right < len(gems):
        if len(elements) == types_nums:
            if len(answer) == 0 or (answer and answer[1]-answer[0] > right-left): # 구간이 짧은 경우에 갱신
                answer = [left+1, right+1]
            
        if elements[gems[left]] > 1:
            elements[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right < len(gems):
                elements[gems[right]] = elements.get(gems[right], 0) + 1
        
    return answer
        
        
    
    
