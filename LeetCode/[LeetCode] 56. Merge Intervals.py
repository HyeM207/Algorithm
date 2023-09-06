# Soltuion 1 (내 풀이) - 실패
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        left = 0
        right = 1
        
        while right < len(intervals) :
            if intervals[left][1] >= intervals[right][0] :
                mergeNode=  [intervals[left][0], max(intervals[left][1],intervals[right][1])]       
                intervals[left], intervals[right] = mergeNode, intervals[right+1]
                del intervals[right]
            else : 
                left += 1
                right += 1 

        return intervals

# 풀이 : 투 포인터를 두어 리스트의 왼쪽부터 오른쪽 끝까지 탐색하면서, merge할 수 있는 조건이 되면 합치는 흐름이다
# 후기 : submit에서 막혔다.. 예외처리를 해줘야 되는데 못해서 그런것으로 보인다. 다음 책 풀이를 참고하여 해결하였다. 


# Solution 2 (책 풀이)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for i in sorted(intervals, key = lambda x: x[0]) :
            if merged and i[0] <= merged[-1][1] :
                merged[-1][1] = max(merged[-1][1], i[1])
            else: 
                merged += i,
        return merged

# 풀이 : merged 라는 리스트를 따로 선언하여 해당 리스트에 merge한 후의 원소들을 저장하는 결과 리스트이다. 
#           - 주어진 리스트 intervals를 정렬한 후 for문으로 하나씩 원소를 빼서 다음 조건에 맞는지 비교하여 조건에 맞는다면,  merged 리스트 마지막에 넣은 원소를 바꾼다.
#               - "조건" : 기존 리스트에서 뽑은 원소의 첫번째 인덱스가 이전 원소의 두번째 인덱스보다 작다면 (merge가 가능하다면)
#           - 조건을 만족하지 않을 경우 merge를 할 수 없다는 뜻이므로, 바로 merged에 원소를 추가한다.
# 
# 후기 : 정렬 챕터의 문제라, 버블정렬, 병합, 퀵 정렬을 이용해서 풀 줄 알았는데 파이썬의 sort, sorted 함수를 사용해서 푸는 문제여서 좋았다. 
