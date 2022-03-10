# Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        str_dict = {}
        
        # 빈도수를 딕셔너리에 기록 
        for c in nums : 
            if c in str_dict :
                str_dict[c] += 1
            else :    
                str_dict[c] = 1
            
        result = []
        
        # 상위 k개 출력 
        tmp = sorted(str_dict.items(), key=lambda x: x[1], reverse=True) # 딕셔너리를 value를 기준으로 내림차순으로 정렬
        for i in range(k) :
            result.append(tmp[i][0])
            
        return result
        