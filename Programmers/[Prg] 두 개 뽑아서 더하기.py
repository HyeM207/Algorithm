# 문제 - lv.1
'''
# #1-230223 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 모든 조합을 구해 합을 구해 리스트에 저장 후, 집합(set)으로 만들어 중복 제거하고 정렬(sorted)한다.
'''

def solution(numbers) :
    hap_array = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)) :
            hap_array.append(numbers[i]+numbers[j])

    return sorted(list(set(hap_array)))