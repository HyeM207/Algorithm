# Solution 1 (내 풀이) - 성공
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right  = 0, len(numbers) - 1
        
        while left >= 0 and left <len(numbers) and right >= 0 and right < len(numbers)  :
            if numbers[left] + numbers[right] > target :
                right -= 1
            elif numbers[left] + numbers[right] < target :
                left += 1
            else :
                return [left+1 , right+1]
            
# 풀이 : 투 포인터를 사용하여 푼 문제이다. 해당 문제의 조건으로 target을 만족하는 쌍이 무조건 있다고 하였으니,
#               왼쪽 포인터 left는 0에서 오른쪽 포인터는 배열의 마지막 인덱스로 하여 
#               두 포인터가 가리키는 합이 target보다 작으면 left +=1 , 크다면 right -=1 로 포인터를 이동해가며 쌍을 찾는다. 

# 후기 : 이전에 풀었던 two sum 1의 문제에서 투 포인터를 이용하여 풀었던 풀이방식이 떠올라 이번 풀이에 적용해보았다. 