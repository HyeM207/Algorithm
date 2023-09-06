# Solution1 - (내 풀이)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s)) 
        t = ''.join(sorted(t)) 
        return s==t

# 풀이 : 파이썬의 정렬 함수 sort를 사용하여 쉽게 풀었다.


# Solution 2 - (책 풀이)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 풀이 : 더 짧은 코드로 푼 책 풀이이다. 파이썬은 리스트도 '==' 연산자로 같은지 비교할 수 있다!