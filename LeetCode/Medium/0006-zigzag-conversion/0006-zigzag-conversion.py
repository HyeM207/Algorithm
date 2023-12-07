class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 각 행씩 배열에 담아서 합치기. (지그재그 형태 코드로 그래도 구현) => O(N)
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

        return ''.join(s for s in answer)