# 문제 - lv.1 
'''
# #1-230418 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : x좌표와 y좌표에 대한 딕셔너리를 만들어 x,y 좌표별로 카운트하고 1인 것을 뽑아 return한다 (So EASY~)
'''
def solution(v):
    answer = []
    x_dict = {}
    y_dict = {}
    
    for i in v: 
        x_dict[i[0]] = x_dict.get(i[0], 0) + 1
        y_dict[i[1]] = y_dict.get(i[1], 0) + 1
    
    for k, v in x_dict.items() :
        if v == 1:
            answer.append(k)

    for k, v in y_dict.items() :
        if v == 1:
            answer.append(k)

    return answer