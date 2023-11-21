class Solution:
    # 풀이 1: 딕셔너리 이용하여 1회 순회
    def romanToInt(self, s: str) -> int:
        """
        값은 딕셔너리화 하고,for문으로 1회만 돌자
            - 1회 돌때 이전 값을 더함
            - 이유: 이전값이랑 현재값 더하여 예외케이스일 수 있음
        """
        symbols = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 ,
                  'IV' : 4, 'IX' : 9, 'XL' : 40 , 'XC' : 90, 'CD' : 400, 'CM' : 900 }
        
        result = 0
        prev = s[0]
        for c in s[1:]:
            if prev and prev+c in symbols:
                result += symbols.get(prev+c, 0)
                prev = None
            else:
                result += symbols.get(prev, 0)
                prev = c   
        result += symbols.get(prev, 0)
        
        return result
    