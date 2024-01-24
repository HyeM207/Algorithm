# 풀이 1 (240124) : 성공
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_trucks = deque()  # (트럭 무게, 내린 시간)
    total_weight = 0
    now = 1

    for truck in truck_weights:
        # 현재 시간에 내려야 하는 트럭 처리
        while on_trucks and on_trucks[0][1] <= now:
            w, out_time = on_trucks.popleft()
            total_weight -= w
            now = out_time

        # 다음 트럭이 다리에 탑승 가능한 경우
        while total_weight + truck > weight or len(on_trucks) + 1 > bridge_length:
            w, out_time = on_trucks.popleft()
            total_weight -= w
            now = out_time

        # 트럭 다리에 탑승
        total_weight += truck
        on_trucks.append((truck, now + bridge_length))
        now += 1

    # 남은 트럭이 다리를 지날 때까지 처리
    while on_trucks:
        w, out_time = on_trucks.popleft()
        total_weight -= w
        now = out_time

    return now
