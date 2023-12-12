class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        풀이 1 : 첫번째 원소 기준 sort reverse-> 
            - 합치는 경우 : [a,b] [c,d] 일때 [a,b]가 [c,d]를 포함하거나 overlap 된 경우 
            - 반대로 안 합치는 경우 : b< c인 경우 
            - 합치는 방법 : 포괄하는 형태. [a, b] 에서 a는 가장 작은 수가 b는 가장 큰 값 
        """
        intervals.sort(key= lambda x : x[0])
        answer = []
        
        for i in intervals:
            if not answer or (answer and answer[-1][1] < i[0]): # 안 합치는 경우
                answer.append(i)
            else:
                answer[-1] = [min(answer[-1][0], i[0]), max(answer[-1][1], i[1])]
        return answer