# 문제 - lv.1
"""
# #1-230608 성공
- 풀이: (아래참고)
- 의문점 : 왜 'if t2 == "00:00":'를 빼야지 풀릴까.. 문제에서 00:00 이후로는 주어지지 않는다고 말은 했는데 신기하군

C, C#, D, D#, E, F, F#, G, G#, A, A#, B 
- #이 문제 => = #이 붙으면 소문자로 변환
- 기억하는 건 음악 끝부분과 처음 부분이 이어서 재생된 멜로디 => 기존의 악보를 앞뒤로 붙여주자 (*3)
- 동일한 것이 여러개 이면 => 제일 긴 것 반환
- !놓친점 : 라디오 시간이 정렬된것이 아니다 => sort()
- !놓친점 : 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다. => 조건추가
"""

def convert_sharp_lower(s):
    """
    #이 붙으면 소문자로 변환
    """
    i = 0
    while i < len(s) :
        if s[i] == '#':
            s  = s[0:i-1] + s[i-1].lower() + s[i+1:]
        i += 1
    return s


def get_time_gap(t1, t2):
    """
    분으로 바꿔서 계산
    """
    time1 = int(t1.split(":")[0])*60 + int(t1.split(":")[1])
    # if t2 == "00:00":
    #     time2 = 24*60
    # else:
    time2 = int(t2.split(":")[0])*60 + int(t2.split(":")[1])
    return time2-time1

def solution(m, musicinfos):
    answer = "(None)"
    answer_len = -1
    listened = convert_sharp_lower(m)
    musicinfos.sort(key=lambda x : x[0].split(",")[0]) # 정렬

    for music in musicinfos:
        start_t, end_t, title, info = music.split(",")
        time_gap = get_time_gap(start_t, end_t)
        # 재생된 시간에 맞게 문자열 재조정
        info = convert_sharp_lower(info) * (len(m)//len(info)+1) 
        info = info[:time_gap+1]  
        # 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디
        info = info * 3 # 앞뒤 추가
        # 문자열이 있다면 조건 만족하는지 체크
        if listened in info:
            if time_gap > answer_len:
                answer = title
                answer_len = time_gap
    return answer
