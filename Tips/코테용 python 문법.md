# 기본 세팅
## input 설정
```
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
```

<br>

# 입력 받기

## 배열 입력 받기
### 크기가 nxn인 2차원 배열
```
nList = [[0] * n for _ in range(n)]
```


### NxN 크기 표 값 입력 (한 칸씩 더 크게 만들기)
```
nList = [ [0] * (n+1) ]

for _ in range(n):
    nList.append([0]+list(map(int, input().split())))
```

### 문자열 Counter 옵션 쓰기



# 딕셔너리
### defaultdict
기본 딕셔너리의 경우 존재하지 않는 키 조회시 KeyError가 든다.
defaultdict의 경우 존재하지 않는 키 조회시 에러 대신에 요소를 생성해준다. 


또한 defaultdict을 이용하면 value로 list를 넣을 수 있다. 

# 라이브러리
## Collection
https://docs.python.org/ko/3/library/collections.html

## Counter
```
import collections
counter = collections.Counter()
# 키추가 
counter['a'] = 0

# 키삭제
del counter['x']
```
counter끼리 교집합,합집합 연산 가능함
xCounter & yCounter # 교집합 
list((xCounter & yCounter).elements()) # 위의 교집합으로 나온 것을 리스트로 바꿀 수 있음 

## Deque

## PriorityQueue
from queue import PriorityQueue
que = PriorityQueue()
que = PriorityQueue(maxsize=8)

que.put(4)
que.put(1)
que.put(7)
que.put(3)
print(que.get())  # 1
print(que.get())  # 3
print(que.get())  # 4
print(que.get())  # 7

# 한줄 for문로 for문 합치기

## 리스트 뒤집기
test[::-1]

## 정렬 함수 (sorted, sort)
sorted(정렬할 리스트, key=len)
sorted(strings, key= lambda x :(x[n], x)) # lambda 로 정렬 기준 정할 수 있고 괄호 사용 시 우선순위 지정가능함

## 대소문자 변형 및 숫자 판단
s.lower()
s.upper()
s.isupper()
s.isdigit()

## if문 여러개 비교 
return True if len(s) in (4,6) else False

## return-if문 한 줄 
return 참일때 보낼값 if 비교문 else 참이아닐때 보낼값
return True if x> 10 else False


## 리스트 문자열로 변환하여  return
return ''.join(sorted(s, reverse=True))

## 아스키코드 <-> 문자
print(chr(97)) # 아스키 -> 문자
print(ord("A")) # 문자 -> 아스키


## 리스트 원소 (remove()와 del 차이)
arr.remove(원소값) # 리턴값은 없고, 없는 원소 값을 넣을 시에는 ValueError 돌려줌
del arr[삭제할 원소 인덱스] 

-> remove는 원소 값으로, del은 원소 인덱스로 접근하여 삭제함

### 진법 변환 
bin() # 2진수
oct() # 8진수
hex() # 16진수

#### 비트 연산
bin(a & b) 
bin(a | b) 
bin(~a) 
bin(a ^ b) 

(bin으로 안 묶고 10진수 그대로 a|b 연산해도 비트 연산된다. )

#### 추가 (format)
format을 이용하면 진수에서 접두어 제외 가능함
format(42, 'b')
'101010'

format(9 | 30,'b')
'11111'


#### 추가 (.zfill())
10진수에서 2진수 변환 시, 고정된 2진수 자릿수를 지정할 때 사용함
format(31 | 14,'b').zfill(n)
'011111'

## 문자열 치환 
text = text.replace("바꿀 문자", "치환할 문자" [,치환 횟수]
)


## for문으로 리스트 2개 출력 -> zip() 이용
for i, j in zip(arr1, arr2) :


### 제곱 연산
2^ 10
=> print(2 ** 10)

## 진법 계산 
answer = int(tmp, 3) # tmp를 3진법으로 계산

## 2차원 배열 정렬
lst.sort(key=lambda x:x[0]) # 0번째 인덱스에 대해서 정렬
lst.sort(key=lambda x: (x[0], -x[1])) #0번째 인덱스에 대해서 오름차순으로 정렬한 뒤, 동일한 값의 경우 내림차순으로 재정렬된다.

### 2차원 배열 내부 정렬
# 내부 리스트 안에서 정렬
for i in range(len(arr)):
    arr[i] = sorted(arr[i])

혹은 max와 min 함수 이용하기
max(min(x) for x in arr)

# set(집합) 연산
& 교집합
+ 합집합
- 차집합



# 반올림 
```python
import math
math.ceil(3.14) # 올림 -> 4
math.floor(3.14) # 내림 -> 3
round(3.14) # 반올림 -> 3 (파이썬에 기본 내장되어, import 할 필요없이 바로 사용가능함)
```