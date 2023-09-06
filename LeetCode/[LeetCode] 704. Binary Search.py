# Solution 1 (내 풀이)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def recursive(left:int ,right:int) -> int :
            if left <= right:
                mid = (left+right) // 2
                if nums[mid] == target :
                    return mid
                elif nums[mid] < target :
                    return recursive(mid+1, right)
                elif nums[mid] > target :
                    return recursive(left, mid-1)
            else :
                return -1
            
        return recursive(0, len(nums)-1)

# 풀이 : 재귀구조를 이용하여 풀이하였다. 파라미터를 찾고자 하는 왼쪽과 오른쪽 인덱스를 두고, 중간값을 target과 비교하여
#       작으면 왼쪽 부분을, 크다면 오른쪽 부분을 탐색하는 코드이다.    