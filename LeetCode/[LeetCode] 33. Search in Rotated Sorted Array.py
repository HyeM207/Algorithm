# Solution 1 - (책 풀이)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :
             return False 
            
            
        # 1. pivot 위치 찾기
        left, right = 0, len(nums) -1 
        while left < right :
            mid = left + (right - left) // 2
            
            if nums[left] > nums[right] :
                left = mid + 1
            else:
                right = mid
        
        pivot = left 
        
        # pivor 기준 이진 검색 
        left, right = 0, len(nums) - 1
        while left <= right : 
            mid = left + (right - left) // 2
            mid_pivot = (mid+pivot) % len(nums)
            
            if nums[mid_pivot] < target :
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else : 
                return mid_pivot
        return -1
        

# 후기 : 문제가 잘 이해되지 않아 시간이 걸렸던 문제이다. 책 풀이를 참고하여 문제 풀이를 이해하였다.
# 풀이 : 먼저 pivot위치를 찾고, pivot을 기준으로 이진 검색을 하게 된다. 
#       1. pivot은 최소값을 찾으면 된다. while문의 조건을 left < right으로 했기에, while문을 빠져나오면 left에는 가장 작은 값이 left가 들어 있을 것이다. 이 값이 pivot이 된다.
#       2. 이진 탐색에서는 mid_pivot으로 값을 비교하게되고, right와 left포인터의 위치는 mid 변수에 의해 조정된다. 