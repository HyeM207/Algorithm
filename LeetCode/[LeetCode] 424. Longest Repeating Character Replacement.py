# Solution 1 - 책 풀이
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = right = 0
        counts = collections.Counter()
        
        for right in range(1, len(s) + 1) : 
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐핵 
            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시 왼쪽 포인터 이동 
            if right - left - max_char_n > k :
                counts[s[left]] -= 1
                left += 1
        
        return right - left 


# 책 풀이 : 오른쪽 포인터는 계속 우측으로 이동하고, 왼족 포인터를 계속 좁혀 범위를 조절해 나간다. 
#          해당 풀이의 핵심은 "max(right) - max(left) - max_char_n == k" 로, 오른쪽에서 왼쪽 포인터 위치를 빼고, 윈도우 내 출현빈도가 가장 높은 문자의 수를 뺀 값이 k와 같으면 가장 큰 최댓값이라 정의할 수 있다는 점이다.
