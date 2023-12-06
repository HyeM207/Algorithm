class Solution:
    # 풀이 1: 이중 for문 => 시간초과
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        while left < right:
            water = (right-left) * min(height[left], height[right])
            answer = max(answer, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return answer