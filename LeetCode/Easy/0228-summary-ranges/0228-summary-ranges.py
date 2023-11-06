class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) < 2:
            return list(map(str,nums))
        
        start_idx = 0
        cur_idx = 1
        is_sorted = False
        result = []
        while cur_idx < len(nums):
            if nums[cur_idx-1] == nums[cur_idx]-1: # 앞뒤가 연속적일 때 
                if not is_sorted :
                    start_idx = cur_idx - 1 
                    is_sorted = True
            else: # 앞뒤가 연속적이지 않을때 
                if is_sorted:
                    result.append(str(nums[start_idx])+ "->" +  str(nums[cur_idx-1])) 
                    is_sorted = False
                else:
                    result.append(str(nums[cur_idx-1]))
            cur_idx += 1
        
        # 마지막 순회 후 작업  
        if is_sorted:
            result.append(str(nums[start_idx])+ "->" +  str(nums[cur_idx-1])) 
        else:
            result.append(str(nums[cur_idx-1]))
        return result