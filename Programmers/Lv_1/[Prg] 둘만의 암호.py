# 문제 - lv.1
'''
# #1-230504 성공
- 풀이: set을 이용해 skip제거한 알파벳 모음 리스트를 만들어서 인덱싱 계산하기
- 참고 : 아스키코드 a=97, z=12
'''
def solution(s, skip, index):
    answer = ''
    alphabet = [ chr(x) for x in range(97,123)]
    final = sorted(list(set(alphabet) - set(skip)))
    
    for i in s :
        idx = (final.index(i)+index)%len(final)
        # print(idx, final[idx])
        answer += final[idx]

    return answer