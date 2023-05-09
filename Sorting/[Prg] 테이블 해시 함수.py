## 문제 - lv.2
'''
# #1-230509
    정확성: 100.0
    합계: 100.0 / 100.0 
    풀이 : 순서대로 구현하면 되는 문제. sort할때 lambda로 하는 것만 유의
'''
'''
문제 설명
1. col번째로 오름차순, 동일시 첫번째 컬럼으로 내림차순
2. S_i = 각 컬럼 값 / i번째행
3. row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR  
'''
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key= lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1) :
        answer ^= sum([d % i for d in data[i-1]])
    return answer