# Solution 1 - (책 풀이)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums :
            result ^= num
            
        return result

# 풀이 : 두 번 등장한 엘리먼트는 0으로 초기화되고, 한 번만 등장하는 엘리먼트는 그 값을 온전히 보존하는 XOR 연산을 이용하여 풀이한 방법이다.
# 후기 : XOR 연산에 이러한 기능이 숨겨져 있는지 몰랐는데, 이번 문제를 통해 새롭게 알게되어 신기하다. 