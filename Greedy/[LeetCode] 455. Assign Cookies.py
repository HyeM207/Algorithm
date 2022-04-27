# Solution 1 - 내 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        i = 0
        j = 0
        result = 0 
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s) :
            if g[i] <= s[j] : 
                result += 1
                i += 1
                j +=1 
            else :
                j += 1
            
        
        return result
'''0 
# 개선사항 (줄 11-20) : 중복되는 코드 제거
while i < len(g) and j < len(s) :
            if g[i] <= s[j] : 
                result += 1
                i += 1
            j += 1
'''
# 풀이 : 단순한 문제로, 각 리스트를 정렬하여, while문을 돌며 g[i] <= s[j] 를 만족하는 경우를 카운트하는 문제이다.
#               (i는 greed factor 리스트의 인덱스 포인터고, j는 각 쿠키 크기 리스트 인덱스 포인터이다.)
# 후기 : 처음에 문제를 잘못 이해하여 돌아갔는데, 감 잡고나니 쉽게 풀린 문제다. 

