# 문제 - lv.2
'''
# #1-230607 성공
    풀이 : 딕셔너리로 중복 체크한 문제 (-> set으로도 풀이 가능해보임)
'''
def solution(n, words):
    answer = [0,0]
    idx = 0 # 단어 인덱스 
    words_dict = {}
    end_c = words[0][0] # 시작키워드
    
    while idx < len(words):
        # 틀린경우
        if words[idx] in words_dict.keys() or end_c != words[idx][0]:
            answer = [idx%n+1, idx//n+1]
            return answer
        # 맞은경우
        end_c = words[idx][-1]
        words_dict[words[idx]] = 1
        idx += 1
            
    return answer