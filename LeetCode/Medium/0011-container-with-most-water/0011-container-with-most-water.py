class Solution:
    # 풀이 1: 투포인터 이용=> 시간 복잡도 O(n), 공간복잡도 O(1)
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