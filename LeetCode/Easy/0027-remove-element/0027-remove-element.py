class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums의 val을 제거하는데 남아있는 nums의 앞에서부터 k개까지는 val이 없어야됨
        # pop을 이용한 풀이 => 시간 복잡도 O(n)
        k = 0
        j = 0
        all_len = len(nums)
        while j < len(nums):
            print(j, nums[j])
            if nums[j] == val:
                nums.pop(j)
                k += 1
            else:
                j += 1
        return all_len-k