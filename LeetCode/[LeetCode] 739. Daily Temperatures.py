# Solution 1 (책 풀이 참고) -- 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        
        # (for문으로 temperatures 한 번만 순회하면서, stack에 인덱스를 저장)
        for i, t in enumerate(temperatures) :
            
            # stack에서 값을 꺼내어, 현재 온도 보다 낮은 것이 있다면 pop하여 result에 날짜 차이를 저장
            while stack and t > temperatures[stack[-1]] : 
                last = stack.pop()
                result[last] = i - last
            
            stack.append(i)
            
        return result 


# Solution 2 (2회독_220608_성공)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 핵심 : stack에 지난 요일의 인덱스를 저장하자
        
        days = [] 
        results = [0] * len(temperatures) 
        
        for i, t in enumerate(temperatures) :
            while days and temperatures[days[-1]] < t: 
                prev_idx = days.pop()
                results[prev_idx] = i - prev_idx
            
            days.append(i)
    
        return results