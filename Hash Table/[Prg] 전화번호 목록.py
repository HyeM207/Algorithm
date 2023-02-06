# 문제 -lv 2 
'''
# #1-230206 실패
# 틀린 이유 : 가장 짧은 문자열만이 접두어가 되는 것이 아님
'''
import collections
def solution(phone_book):
    
    test = collections.Counter(phone_book)
    
    # 1. 요소 길이순으로 정렬
    phone_book.sort(key=len)
    
    # 2. 가장 짧은 문자열 길이만큼 각 요소를 슬라이딩하여 딕셔너리 키 값 저장 
    dict = {}
    min_len = len(phone_book[0])
    for p in phone_book:
        p_key = p[:min_len]
        
        if not p_key in dict.keys():
            dict[p_key] = 1
        else :
            return False
    
    return True