# 문제 - lv.2
'''
# #1-230516
    정확성: 100.0
    합계: 100.0 / 100.0 
    풀이 : 방 리스트를 만들어, 원소로 입장가능한 시간을 분으로 바꿔 저장함
    개선점 :  타임라인으로 푸는 것이 더 효율적일듯하다
'''
def time_to_minutes(leave_time, added=0) :
    hour, minutes = map(int, leave_time.split(":"))
    return hour*60 + minutes + added
    
    
def solution(book_time):
    answer = 0
    book_time.sort(key= lambda x: x[0])
    room_list = []
    # print(book_time)
    
    for book in book_time:
        check_out = time_to_minutes(book[1],10)
        if len(room_list) == 0 :
            room_list.append(check_out)
        else:
            room_list.sort()
            check_in = time_to_minutes(book[0])
            is_room = False
            for i in range(len(room_list)):
                if room_list[i] <= check_in : 
                    room_list[i] = check_out
                    is_room = True
                    break
            if is_room == False : 
                room_list.append(check_out)
    return len(room_list)