## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 3중for문으로 푼 비효율적코드이다. 추후 개선 필요
'''
def solution(number):
    answer = 0
    # 노가다 (3중for문 - 비효율적)
    for i in range(0, len(number)-2) :
        for j in range(i+1, len(number)-1):
            for z in range(j+1, len(number)):
                if number[i] + number[j] + number[z] == 0 :
                    answer +=1 
    return answer