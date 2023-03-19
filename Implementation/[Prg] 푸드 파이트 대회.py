## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 앞단의 문자열은 주어진 음식양을 2로 나눈 몫의 개수만큼 존재한다는 규칙을 이용하여 풀이함
'''
def solution(food):
    front = ''
    for i in range(1,len(food)):
        front += str(i) * (food[i]//2)               
    
    return front + "0" + front[::-1]