# Solution 1 - 책 풀이
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 책 풀이
        heap = []
        
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
            
    
        result = []
        
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
            
        return result

# 풀이 : 우선순위 큐를 이용해 순서대로 값을 추출하여 해당 인덱스에 insert하는 풀이이다.
#       핵심은 people의 원소의 첫 번째 값이 "큰 순서대로 추출되는 최대 힙 형태"로 풀이하였고,
#`      최대 힙 형태로 구현하기 위해 첫번째 값을 heapq에 넣을 때 음수로 변환한다.
#       두 번째로는 "인덱스"를 하여 삽입되는 위치로 구현하였다.`


# 후기 : heapq를 이용하여 어떻게 구현할까 생각했는데, 책 풀이를 보고나니 풀이가 대단하게 느껴졌다.
