def solution(s):
    answer = ''
    is_first = True
    for i in range(len(s)):
        c = s[i]
        if c ==  " " :
            is_first = True
            answer += c
            continue
        if c.isalpha():
            if is_first :
                c = c.upper()
            else:
                c = c.lower()
        is_first = False
        answer += c
            
    return answer