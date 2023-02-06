# 문제 - lv1
'''
# #1_230206 성공 
    정확성: 100.0
    합계: 100.0 / 100.0
    :  collections의 Counter 이용한 간단히 풀이
'''
import collections 
def solution(nums):
    
    p_hash = collections.Counter(nums)
    nums_len = len(nums)/2
    p_len = len(p_hash.keys())
    
    if nums_len <= p_len : 
        return nums_len
    
    return p_len
        
'''
# #2_230206 성공 
    정확성: 100.0
    합계: 100.0 / 100.0
    : (풀이 참고) counter가 아닌 set를 써도 가능하다. min함수 까지 이용하면 더더욱 간단하다 (기억하자!)
'''
def solution(nums):
    return min(len(nums)/2, len(set(nums)))