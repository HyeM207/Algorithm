class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 영어 잘 읽기. nums1을 수정해야됨!
        nums1[m:]  = nums2[:n]
        nums1.sort()