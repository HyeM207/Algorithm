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