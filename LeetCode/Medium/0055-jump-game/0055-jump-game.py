class Solution:
    # 풀이1 : 가다가 자기 남은 jump보다 크면 update => 시간 O(n) 공간 O(1)
    # 갈수 있는거리 중 최대값으로 가면됨
    def canJump_(self, nums: List[int]) -> bool:
        jump = 0
        for idx, n in enumerate(nums):
            jump = max(jump, n)
            if jump >= len(nums)-idx-1:
                return True
            if jump <= 0 : 
                return False
            jump -= 1
        return True if jump > 0 else False
    
    
    # 풀이 2: 풀이 1을 개선한 코드 (Greedy) => 시간 O(n) 공간 O(1)
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0 # 갈 수 있는 최대거리
        last_pos = len(nums) - 1 # 마지막 원소 인덱스

        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])

            if max_reachable >= last_pos:
                return True

        return False