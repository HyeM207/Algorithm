class Solution:
    # 풀이 1
    def findPeakElement(self, nums: List[int]) -> int:
        """
        이진탐색 풀이 
            - left, right, mid 포인터 이용
            - 조건에 따라 왼쪽, 오른쪽 탐색 실행 (조건 : 중간 값 기준으로 양옆 이웃 비교함)
        """
        def max_index(left, right):
            """ 값 비교 후 더 큰 값의 인덱스 반환 """ 
            if nums[left] < nums[right]:
                return right
            return left

        left, right = 0, len(nums)-1
        answer = max_index(left, right)

        while left < right:
            mid = (left + right) // 2
            answer = max_index(answer, mid)
            if nums[mid-1] < nums[mid+1]: # 오른쪽 탐색 
                left = mid+1
                answer = max_index(answer, left)
            else: # 왼쪽 탐색 
                right = mid-1
                answer = max_index(answer, right)
                
        return answer