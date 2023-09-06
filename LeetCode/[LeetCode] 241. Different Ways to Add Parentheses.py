# Solution 1 - (책 풀이)
class Solution :    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # eval 함수로 문자열의 식을 계산함
        def compute(left, right, op):
            results = []
            for l in left :
                for r in right :
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        # 분할 결과를 리턴받으려면 input이 숫자형일 때 리턴함 
        if expression.isdigit() : 
            return [int(expression)]
        
        results = []
        
        # 연산자를 기준으로 재귀로 left, right를 계속 분할하고, 분할된 값은 compute 함수로 계산한 결과를 extend로 확장함
        for index, value in enumerate(expression) :
            if value in "-+*" :
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                
                results.extend(compute(left, right, value))
                               
        return results

# 후기 : 도저히 어떤 식으로 접근해야 될 지 모르겠어서 책 풀이를 참고하였다. 다음 2회독때는 혼자 힘으로 풀 수 있도록 풀이를 마스터해야겠다. 
# 풀이 : 해당 풀이의 핵심은  연산자를 기준으로 재귀로 left, right를 계속 분할하고, 분할된 값은 compute 함수로 계산한 결과를 extend로 확장한다는 것이다. 


