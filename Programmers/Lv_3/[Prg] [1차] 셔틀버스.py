# 풀이 1 (240126) : 성공

def minutes_to_time(minutes):
    hours, mins = divmod(minutes, 60)
    return f"{format(hours, '02')}:{format(mins, '02')}"

def time_to_minutes(time):
    hours, mins = map(int, time.split(":"))
    return 60*hours + mins
    

def solution(n, t, m, timetable):
    # 1. 버스 테이블 분으로 만들기
    first_bus = 540
    last_bus = first_bus + (n - 1) * t
    bus_table = [first_bus + i * t for i in range(n)]

    # 2. timetable 분으로 바꾸기
    timetable_mins = [time_to_minutes(t) for t in timetable]
    timetable_mins.sort()

    # 3. 마지막 버스에 탈 수 있는 승객 계산
    t_p = 0 #마지막 버스 타는 손님 가리키는 포인터
    for bus in bus_table:
        cnt = 0
        flag = False
        for i in range(t_p, len(timetable)):
            if cnt >= m or bus < timetable_mins[i]:
                flag = True
                break
            cnt += 1
        t_p = i
        if bus == bus_table[-1] and flag: # 마지막 버스에 탈 수 있는 승객 중 가장 늦게 온 승객의 시간을 가리키도록 하기 위함
            t_p -= 1
    
    # 4. 마지막 버스에 자리가 남았다면 마지막 버스 시간 반환
    if cnt < m:
        return minutes_to_time(last_bus)

    # 5. 마지막 버스에 자리가 없다면 마지막 승객보다 1분 일찍 도착
    return minutes_to_time(timetable_mins[t_p] - 1)
