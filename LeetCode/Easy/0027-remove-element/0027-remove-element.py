class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums의 val을 제거하는데 남아있는 nums의 앞에서부터 k개까지는 val이 없어야됨
        # 투포인터를 이용하여 val을 발견하면 뒤를 가르키는 포인터 위치와 val 위치를 swap함
        last_p = len(nums) -1 
        now_p = last_p
        k = 0
        while now_p >=0:
            if nums[now_p] == val:
                nums[now_p], nums[last_p] = nums[last_p], nums[now_p]
                k += 1
                last_p -= 1
            now_p -= 1
        
        return len(nums) - k
            
        