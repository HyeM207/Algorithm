# 문제 - lv.2
'''
# #1-230503 실패
    >> 다시 풀어야 함
    합계 : 테스트 코드는 맞는데 제출 누르면 절반이상이 틀림 -> 알고리즘 전반적 개선 필요
    풀이 : deque에 다리에 올라간 차 무게와 오른 시간을 같이 저장한다
        - for문으로 트럭한대씩 접근하여 올라갈 수 있는지 없는지 if문으로 판단하고,
        - 올라갈 수 있으면 올라가되, 만약 다리에서 올라간 차가 이미 시간이 지났는데도 있으면 빼낸다
        - 올라갈 수 없으면 올라갈 수 있도록 pop하고 차를 올린다. 이때도 이미 시간이 경과됐는데도 있으면 빼낸다.
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    moving =  deque()
    sum_moving = 0
    time = 0
    
    for truck in truck_weights : 
        time+=1   
        # print(f'[{truck}] 경과 시간 : {time} sum_moving : {sum_moving} {moving}')
        if sum_moving + truck <= weight : 
            while moving and moving[0][0] < time : 
                sum_moving -= moving.popleft()[1]
            moving.append([time, truck])
            sum_moving += truck
            # print(f'과정 1 시간 : {time} sum_moving : {sum_moving} {moving}'/)
        else : 
            left = moving.popleft()
            time = left[0] + bridge_length
            sum_moving -= left[1]
            while moving and moving[0][0] < time : 
                sum_moving -= moving.popleft()[1]
            moving.append([time, truck])
            sum_moving += truck
            # print(f'과정 2 시간 : {time} sum_moving : {sum_moving} {moving}')
    print("마지막" , moving)