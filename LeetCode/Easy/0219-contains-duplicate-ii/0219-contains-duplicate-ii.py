class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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
                