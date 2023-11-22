# 2023 KAKAO BLIND RECRUITMENT
# 풀이1 : 문자열(년,월,일) 그대로 계산
def get_end_date(terms: dict, start_time: str, t_type: str) -> str:
    """
    유효기간 계산함수
    """
    year, month, date = map(int, start_time.split("."))
    month += terms[t_type]
    date -= 1
    
    if date < 1:
        month -= 1
        date = 28
    if month > 12:
        year += month // 12
        month = month % 12
    if month < 1: # elif가 아닌 if로 두기
        year -= 1
        month = 12 + month 
    end_date = f"{year:04d}.{month:02d}.{date:02d}"
    return end_date

def is_over(today:str, end_date:str) -> bool:
    """
    날짜 크기 비교 함수 
    """
    t_year, t_month, t_date = map(int, today.split("."))
    e_year, e_month, e_date = map(int, end_date.split("."))
    if t_year > e_year:
        return True
    elif t_year < e_year:
        return False
    if t_month > e_month:
        return True
    elif t_month < e_month :
        return False

    return t_date > e_date
    
def solution(today, terms, privacies):
    answer = []
    
    # 1) terms 딕셔너리화
    terms_dict = {}
    for term in terms:
        _type, due = term.split(" ")
        terms_dict[_type] = int(due)  

    # 2) 유효기간 확인
    for idx, privacy in enumerate(privacies):
        start_date, _type = privacy.split(" ")
        end_date = get_end_date(terms_dict, start_date, _type)
        if is_over(today, end_date):
            answer.append(idx+1)
    return answer


# 풀이 2: 날짜로 '일'로 바꾸어 계산(다른 사람 풀이 참고)
def to_days(date):
    # '일'로 바꿈
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
