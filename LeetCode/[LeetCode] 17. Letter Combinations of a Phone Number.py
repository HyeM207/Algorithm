# Solution 1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 다이얼 딕셔너리
        graph = {
            '2' : ['a','b','c'], 
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }

        def dfs (index, path)  :
            if len(path) == len(digits):
                result.append(path)
                return 
            
            for i in range(index, len(digits)):
                for c in graph[digits[i]] :
                    dfs(i+1, path+c)
                    
                    
        if digits == "" :
            return []
        
        result = []
        dfs(0, "")
        
        return result

# 풀이 (책 참고) : dfs를 이용한 문제로, dfs함수가 호출되면 for문으로 주어진 문자열에 해당하는 값을 추가하게 된다. 만약 만든 문자열이 해당 길이를 만족하면 return 된다. 