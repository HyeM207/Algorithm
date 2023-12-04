class Solution:
    # 풀이 1: pop과 append를 이용한 풀이
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums) 
 
        prev_num = nums[0]
        prev_cnt = 1
        idx = 1
        dup_cnt = 0
        while idx < len(nums)-dup_cnt:
            if prev_num != nums[idx]:
                prev_num = nums[idx]
                prev_cnt = 1
                idx += 1    
            else:
                prev_cnt += 1
                if prev_cnt > 2:
                    nums.append(nums.pop(idx))
                    dup_cnt += 1
                else: 
                    idx += 1
                    
        return len(nums)-dup_cnt

#     # 풀이2 : 인덱스를 이용한 풀이
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return len(nums)
        
#         idx = 2  # 중복이 최대 2개까지만 허용되므로 인덱스 2부터 시작
        
#         for i in range(2, len(nums)):
#             if nums[i] != nums[idx - 2]:  # 중복이 최대 2개까지만 허용되므로 두 칸 이전의 요소와 비교
#                 nums[idx] = nums[i]
#                 idx += 1
        
#         return idx