
# 문제 - lv.2
'''
# #1-230427 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 입출차 내역을 딕셔너리화 하고 시간을 문자열화하여 계산 후, 요금을 계산하면 된다.
        - 놓친 부분 : 차량 중복 가능, 차량번호 낮은 번호부터 사용
    개선 사항 : 
        - 딕셔너리에서 키 있는지 확인하는 것 대신 .get() 이나 defaultdict() 활용하기 
'''
import math

def time_to_minutes(time) -> int:
    minutes = int(time[0]) * 600
    minutes += int(time[1]) * 60
    minutes += int(time[3:])
    return minutes


def solution(fees, records):
    answer = [] 
    d = {}
    
    # 딕셔너리화
    for r in records : 
        time, car, inout = r.split(" ")
        if inout == "IN" :
            if car not in d.keys() :
                d[car] = [time]
            else : 
                d[car].append(time)
        else :
            d[car].append(time)
    
    d = dict(sorted(d.items()))

    
    # 요금 계산 
    for car in d.keys():
        # 시간 차이 계산
        if len(d[car])%2 == 1 : 
            d[car].append("23:59")
        gap = 0
        for i in range(0,len(d[car]),2) : 
            gap +=  time_to_minutes(d[car][i+1]) - time_to_minutes(d[car][i])            

        # 요금 계산
        if gap <= fees[0] : 
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((gap - fees[0]) / fees[2]) * fees[3])
            
    return answer