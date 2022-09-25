# 문제 : 주어진 배열을 버블 정렬할 시, swap 한번도 일어나지 않은 루프가 언제인지 알아보기
# 책 풀이 참고
import sys
input = sys.stdin.readline
 
n = int(input())
a = []

for i in range(n):
    a.append( (int(input()), i) ) # 핵심 1 : 저장할 때 인덱스도 같이 저장한다. 

sorted_a = sorted(a) 

max_diff = 0 

pointer = 0
for i in range(n):
    if max_diff < sorted_a[i][1] - i: # 핵심 2 : 정렬 전과 후의 인덱스 차이 최댓값 찾는다.
        max_diff = sorted_a[i][1] - i

print(max_diff+1)

# 풀이 : (책 풀이 참고) 정렬전과 정렬되지 전의 index 차이의 최댓값을 찾고 + 1하면 구하고자 하는 답이다.
#       +1하는 이유는 swap이 일어나지 않는 반복문이 한 번 더 실행되는 것을 감안하여 +1 한다.