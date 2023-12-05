class Solution:
    # 풀이1 : 가다가 자기 남은 jump보다 크면 update
    # 갈수 있는거리 중 최대값으로 가면됨
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for idx, n in enumerate(nums):
            jump = max(jump, n)
            if jump >= len(nums)-idx-1:
                return True
            if jump <= 0 : 
                return False
            jump -= 1
        return True if jump > 0 else False