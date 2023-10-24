class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # pop 을 이용한 풀이 => O(n)
        i = 0
        while i < len(nums): 
            if i>0 and nums[i-1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        print(nums)