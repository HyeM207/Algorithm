class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 풀이1 : 단순 슬라이싱하여 대체
        # 시간 복잡도 O(N), 공간 복잡도 O(N)
        # length = len(nums)
        # k =  k % length
        # nums[::] = nums[length-k:] + nums[0:length-k]
        
        # 풀이2 : 뒤집기 (Solution 참고) : 전체 뒤집기 -> k기준 앞과 뒤 각각 뒤집기
        # 시간 복잡도 O(N), 공간 복잡도 O(1)
        def rotate(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1 
            
        length = len(nums)
        k %= length
        rotate(0, length-1)
        rotate(0, k-1)
        rotate(k, length-1)
        