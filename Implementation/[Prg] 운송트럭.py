# 문제 - lv.1 
'''
# #1-230418 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 상품 가격표를 딕셔너리화 하여 예산 대비 트럭수를 계산한다 (So EASY~)
'''
def solution(max_weight, specs, names):
    answer = 1
    d = {}
    
    for item in specs : 
        d[item[0]] = int(item[1])


    # 상품 순서대로 운반 
    weight = 0
    for item in names : 
        if weight + d[item] > max_weight : 
            weight = d[item]
            answer += 1
        else :
            weight += d[item]
        
    return answer