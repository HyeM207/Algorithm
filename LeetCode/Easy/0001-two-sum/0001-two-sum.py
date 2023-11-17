class Solution:
    # 풀이1. 이중 for문 (O(N^2))
    def twoSum_(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
                
    # 풀이 2. 딕셔너리화 -> 정렬 후 투포인터로 합 더하기 => O(n log n)
    def twoSum_(self, nums: List[int], target: int) -> List[int]:
        # 1) 딕셔너리화 및 정렬
        # 이때 중복된 값이 들어갈 수 있으므로 배열로 인덱스 위치 저장 
        index = {}
        for i, n in enumerate(nums):
            index[n] = index.get(n, []) + [i] 
        
        nums.sort()
        
        # 2) 정렬 후 투포인터로 합 더하기
        left, right = 0, len(nums)-1
        while left<right:
            if nums[left] + nums[right] == target:
                break 
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        # 같은 값을 더하는 경우 예외 처리해줌
        return index[nums[left]]+ index[nums[right]] if nums[left]!=nums[right] else index[nums[left]]
    
    
    # 풀이 3. 1회 순회와 해시맵 이용 => O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap: # 해시맵을 이용하여 탐색 시간 줄임
                return [i, hashmap[complement]]
            hashmap[num] = i
        