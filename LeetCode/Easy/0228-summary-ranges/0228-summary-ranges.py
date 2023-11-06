class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # 풀이 1: 1회 순회하며 if문으로 모든 조건 확인 (정렬 여부와 정렬시 시작 인덱스, 현제 인덱스 사용함)
#         if len(nums) < 2:
#             return list(map(str,nums))
        
#         start_idx = 0
#         cur_idx = 1
#         is_sorted = False
#         result = []
#         while cur_idx < len(nums):
#             if nums[cur_idx-1] == nums[cur_idx]-1: # 앞뒤가 연속적일 때 
#                 if not is_sorted :
#                     start_idx = cur_idx - 1 
#                     is_sorted = True
#             else: # 앞뒤가 연속적이지 않을때 
#                 if is_sorted:
#                     result.append(f"{nums[start_idx]}->{nums[cur_idx-1]}")
#                     is_sorted = False
#                 else:
#                     result.append(str(nums[cur_idx-1]))
#             cur_idx += 1
        
#         # 마지막 순회 후 작업  
#         if is_sorted:
#              result.append(f"{nums[start_idx]}->{nums[cur_idx-1]}")
#         else:
#             result.append(str(nums[cur_idx-1]))
#         return result
    
        # 풀이 2 : 이중 while문으로 정렬 체크
        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            end = nums[i]
            while i < len(nums) -1 and nums[i]+1 == nums[i+1]:
                i += 1
                end = nums[i]
            if start==end:
                result.append(str(start))
            else:
                result.append('->'.join([str(start), str(end)]))
            i += 1
        return result