# Solution 1 - 내 풀이 (실패)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = left + k
        result = []
        max_value = max(nums[left:right])

        while right < len(nums) + 1  :
            print((nums[left:right])) 
            if max_value < nums[right-1] : 
                max_value = nums[right-1] 
                result.append(max_value)
            # result.append(max(nums[left:right]))
            left += 1 
            right += 1
            # print("l : ", left, "r : ", right)

        return result 

# 설명 : 슬라이딩 윈도우에서 가장 큰 값 찾는 문제 
# 풀이 : 단순한 브루트포스로는 풀리지 않아, 큰 값이 들어오면 교체해주는 것으로 코드를 수정했는데, window 크기를 고려하지 않아 실패했다.

# Solution 2 - 책 풀이
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        
        for i, v in enumerate(nums) : 
            window.append(v)
            if i < k - 1:
                continue
                
            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf') : 
                current_max = max(window)
            elif v > current_max :
                current_max = v
            
            
            results.append(current_max)
            
            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
            
        return results                                                         

# 책 풀이 : for문을 돌며 리스트 전체를 조회하는데, 이때 모든 값을 window append,pop하고, 
#           현재 윈도우에서 가장 큰 값을 current_max에 넣고, 만약 윈도우에서 빠지게 되면 float('-inf')로 바꾸고 다음 턴에 max로 새 최대값을 계산한다.

# 즉, 가급적 최댓값 계산을 최소화하기 위해 이전의 최댓값을 저장해뒀다가 한 칸씩 이동할 때 새 값에 대해서만 더 큰 값인지 확인하고,
#   최댓값이 윈도우에서 빠지게 되는 경우에만 다시 전체를 계산하는 형태이다. 