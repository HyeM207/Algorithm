class Solution:
    # 풀이 1: 딕셔너리를 활용한 구현
    def containsNearbyDuplicate_(self, nums: List[int], k: int) -> bool:
        """
        문제 해석 : k 거리 사이에 i와 j 인덱스의 값이 같은지 확인
        [1,2,3,1,2,3,3]
        딕셔너리에 key는인덱스, 값은 값을 넣고,
        for문으로 한 번 순회하면서 인덱스 값을 최신것으로 갱신한다.
        """
        indexs = {}
        if k == 0:
            return False
        for idx, n in enumerate(nums):
            if n in indexs and idx - indexs[n] <= k:
                return True
            indexs[n] = idx
        return False
    
    
    # 풀이2. Set을 이용한 슬라이딩 윈도우
    """
    왼쪽과 오른쪽 포인터로 슬라이딩 윈도우 형성.
    set으로 슬라이딩 윈도우 고유한 원소 저장
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        a = set() # 슬라이딩 윈도우 내의 원소를 중복 없이 저장
        for R in range(len(nums)): # R은 nums 인덱스 
            if R - L > k: # 슬라이딩 윈도우 크기가 k보다 크면 크기 다시 설정
                a.remove(nums[L])
                L += 1
            if nums[R] in a: # 검증
                return True
            a.add(nums[R]) # 슬라이딩 윈도우 안에 들면 원소 add
