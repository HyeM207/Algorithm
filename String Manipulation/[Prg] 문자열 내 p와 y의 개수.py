# 문제 - lv.1
'''
# #1 - 230214 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : for문으로 문자 하나씩 접근하고 p와 y개수를 딕셔너리로 저장
'''
def solution(s):
    char_dict = { 'p' : 0, 'y' : 0}

    for c in s:
        if c.lower() == "p":
            char_dict['p'] += 1
        elif c.lower() == "y":
            char_dict['y'] += 1
    
    return True if char_dict['p'] == char_dict['y'] else False

'''
개선된 코드는 count() 함수를 써서 아래 처럼 한 줄로 풀이 가능하다. (programmers 풀이 참고함)
    return s.lower().count('p') == s.lower().count('y')
'''