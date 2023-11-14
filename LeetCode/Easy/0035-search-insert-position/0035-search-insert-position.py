class Solution:
    """
        target이 있으면 인덱스를 없으면, 넣어야되는 인덱스 반환
        - 탐색 시간 제한있음
        - 반으로 나눠서 탐색하는 분할 탐색 
    """
    # 풀이1 : 만든 재귀함수 이용
    def searchInsert_(self, nums: List[int], target: int) -> int:
        def search(left, right, target):
            # 1) 타켓이 없을 경우 삽입할 인덱스 리턴
            if left > right:
                return left
            
            # 2) left, right 중앙값 검사
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            
            # 3) 중앙값에 따라 탐색할 범위 조정
            if nums[mid] > target:
                result = search(left, mid-1, target)
            elif nums[mid] < target:
                result = search(mid+1, right, target)
            return result
        
        return search(0, len(nums)-1, target)
    
    # 풀이 2: 간단하게 풀이
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1 
            else:
                return mid
        return left