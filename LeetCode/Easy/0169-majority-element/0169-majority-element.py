class Solution:
    def majorityElement_(self, nums: List[int]) -> int:
        """
        목표 : O(1)
        1. sort해서 앞에서 부터 카운트 -> 최소 O(n/2+NlogN)) ~ O(n+NlogN)
        2. Counter 및 딕셔너리화 하여 선별 -> O(n)
        """
        # 풀이1. 1. sort해서 앞에서 부터 카운트
        nums.sort()
        now_num = nums[0]
        cnt = 1
        for n in nums[1:]:
            if n == now_num:
                cnt+=1
                if cnt >= len(nums)/2:
                    return n
            else:
                now_num = n
                cnt = 1
        return now_num
    
        # 풀이2. 정렬 시 majority 원소는 개수가 많으니 중간에 있음 
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]