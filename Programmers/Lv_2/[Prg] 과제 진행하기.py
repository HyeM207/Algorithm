def transfer_to_min(str_time):
    """
    시간을 모두 분 단위로 바꿈
    """
    h, m = str_time.split(":")
    minutes = 60*int(h) + int(m)
    return minutes

def solution(plans):
    answer = []
    delayed = [] # 밀린 과목 [과목명, 남은 시간]
    plans.sort(key= lambda x : x[1])# 정렬
    
    for idx, [subj, start_t, play_t] in enumerate(plans):
        play_t = int(play_t)
        start_t = transfer_to_min(start_t)
        if idx+1 < len(plans):
            left_min = transfer_to_min(plans[idx+1][1]) - start_t
            left_after_play = left_min - play_t
        else: #뒤에 처리할 과목이 없음(마지막 원소일때)
            answer.append(subj)
            break

        if left_after_play < 0: # 다 처리 못함
            delayed.append([subj, play_t-left_min])
            continue
        answer.append(subj)
        if left_after_play > 0 :  # 처리하고도 시간이 남음
            while delayed and left_after_play > 0:
                if left_after_play - delayed[-1][1] >= 0: # 하나 모두 처리 가능
                    left_after_play -= delayed[-1][1]
                    answer.append(delayed.pop()[0])
                else:
                    delayed[-1][1] = delayed[-1][1] - left_after_play 
                    left_after_play = -1
    while delayed:
        answer.append(delayed.pop()[0])
    return answer
