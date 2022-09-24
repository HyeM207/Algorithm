# 문제 : 입력 받는 수를 저장하되, 0이면 저장된 배열에서 절댓값이 가장 작은 값을 출력한다.
# 내 풀이 (책에서 정렬 방법 참고) - 성공 
from queue import PriorityQueue
n = int(input())
mydeque = PriorityQueue()

for _ in range(n):
    _input = int(input())

    if _input == 0 :
        if mydeque.empty():
            print("0")
        else : 
            print(str(mydeque.get()[1]))
    else :
        mydeque.put((abs(_input), _input))

# 풀이 : 자동정렬해주는 우선순위 큐를 이용함
# 핵심 : 우선순위 큐에 저장할 때 mydeque.put((abs(_input), _input))를 이용하여, 정렬이 절댓값 그리고 입력받은 수 대로 정렬되도록 한다. 