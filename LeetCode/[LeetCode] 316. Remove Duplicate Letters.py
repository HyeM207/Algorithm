# Solution 1 (책 풀이 참고) -- 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        counter, stack = collections.Counter(s), []
        
        print(counter)
        
        for char in s :
            
            counter[char] -= 1
            
            if char in stack :
                continue    
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            
            stack.append(char)
            
        return ''.join(stack)


# Solution 2 (2회독_220608_실패 : 책 풀이 참고)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str: 
        counter = Counter(s) # 문자 개수 저장 딕셔너리
        stack = [] # 최종 문자 저장 
        seen = set() # 한 번 처리한 문자 저장 집합 # !핵심!
        
        for c in s :
            counter[c] -= 1
            if c in seen : 
                continue             
            # 이전에 담은 문자가 현재 문자보다 크고, 뒤에 문자가 또 있다면 스택에서 제거
            while stack and c < stack[-1] and counter[stack[-1]] > 0 : # !핵심!
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)

# 후기 : 어떤식으로 알고리즘을 짜야될지 막막했던 문제. 