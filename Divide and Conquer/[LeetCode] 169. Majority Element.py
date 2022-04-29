# Solution 1 - 내 풀이
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]
# 풀이 : 파이썬의 collections.Counter모듈을 이용하여 풀이하였다. 


# Solution 2 - 책 풀이 (분할 정복 방법)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums :
            return None 
        
        if len(nums) == 1 : 
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

# 풀이 : 해당 단원이 분할 정복이므로, 해당 풀이를 가져와봤다. 최소 단위가 될때 까지 쪼개준 다음에 백트래킹 될 때(정복) 때,
#       return [b, a][nums.count(a) > half] 으로 과반수가 넘는 숫자를 return한다.
#       설명을 덧붙이자면, nums 에서 a가 과반수를 차지 한다면 해당 인덱스는 1이 되므로 a를 리턴하게 된다. 



# Solution 3 - 책 풀이 (빠르고 간단한 풀이)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
# 풀이 : 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트인 점을 이용한 풀이이다. 
