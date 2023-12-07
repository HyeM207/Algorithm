"""
    numRows=1
    0 1 2 3 4 5

    numRows=2
    0 2 4 6 8 10  
    1 3 5 7 9

    numRows=3
    0   4   8 
    1 3 5 7 9  
    2   6   10

    numRows=4 
    0    6       12  
    1  5 7    11 13  
    2 4  8 10    14
    3    9       15
"""
class Solution:
    def convert_(self, s: str, numRows: int) -> str:
        # 풀이 1 :각 행씩 배열에 담아서 합치기. (지그재그 형태 코드로 그래도 구현) => O(N)
        if numRows == 1:
            return s
        
        answer = [''] * numRows
        i = 0 
        is_downward = True
        row_idx = 0
        
        while i < len(s):
            answer[row_idx] += s[i]
            if row_idx == numRows-1 and is_downward: # 방향전환 (아래->위)
                is_downward = False
            if row_idx == 0 and is_downward==False: # 방향전환 (위->아래)
                is_downward = True
            
            if is_downward : 
                row_idx += 1
            else:
                row_idx -= 1
            i += 1

        return ''.join(answer)

    # 풀이 2 : 풀이 1에서 행을 바꿀 때 조건문을 사용하는 대신에 행을 증가 또는 감소시키는 값 자체를 조절하는 것으로 변경
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        answer = [''] * numRows
        row_idx, step = 0, 1

        for char in s:
            answer[row_idx] += char
            if row_idx == 0:
                step = 1
            elif row_idx == numRows - 1:
                step = -1
            row_idx += step

        return ''.join(answer)
