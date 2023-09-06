# 문제 - lv.1
'''
# #1-230216 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 처음에는 ord(), chr()를 이용해 아스키코드로 풀려고 했지만 실패했다. 
        그래서 알파벳 딕셔너리와 리스트를 이용하여 풀었다.
'''
def solution(s, n):
    answer = ""
    
    alpha_dict = {chr(c) : c-65 for c in range(65,91)} # len : 26
    alpha_list = [chr(c) for c in range(65,91)]
    
    
    for c in s:
        if c != " ":
            tmp = alpha_list[(alpha_dict[c.upper()] + n )% 26]
            answer += tmp.upper() if c.isupper() else tmp.lower() 
        else :
            answer += c
            
    return answer

'''
(더 나은 풀이) - programmers 다른 사람 풀이
    # 아스키코드를 이용한 풀이이다.
    # 나는 저 식을 짜지 못했는데, 26의 몫을 구해 다시 'A'나 'a'의 아스키 값을 더하는 식을 기억하자.
    def caesar(s, n):
        s = list(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
            elif s[i].islower():
                s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

        return "".join(s)

'''