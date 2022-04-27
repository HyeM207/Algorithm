# Solution 1 - 책 풀이
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            # 개수 순 추출 
            for task, _ in counter.most_common(n+1) : # 핵심 : n+1
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                
            if not counter :
                break

            result += n - sub_count + 1

        return result 

# 책 풀이 : heapq만으로 구현하기에는 count를 따로 해줘야되기 때문에, 본 풀이에서는 Counter 모듈을 사용하였다. 
#          Input 값이 ["A","A","A","B","B","B"], 2 라면, counter는  Counter({'A': 3, 'B': 3})가 된다.
#          for문에서 most_common(n+1)을 하여, n+1개가 추출될 때 idle 없이 실행한다.
#          while문을 반복해가며 counter에 값이 없을 때까지 반복해나간다. 
#          n - sub_count + 1 을 통해 idle 개수를 계산하고 이를 result에 더해 카운트 수를 누적해간다. 


# 모듈 설명 : 
#       - counter.most_common() : 가장 개수가 많은 아이템부터 출력하는 함수 
#       - counter += collections.Counter() :  0 이하인 아이템을 목록에서 완전히 제거