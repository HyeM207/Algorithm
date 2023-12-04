class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 풀이1 : 단순 슬라이싱하여 대체
        length = len(nums)
        k =  k % length
        nums[::] = nums[length-k:] + nums[0:length-k]