## Graph
1. 먼저 DFS인지 BFS 문제인지 판단.
2. 함수의 파라미터를 생각해보며,
3. DFS를 돌며 어떤 값이 적용되어야 하는지 생각해본다.(더해지는 값이나 달라지는 점 주목)
   달라지는 값을 for문과 함수의 파라미터를 이용하면 대부분 풀릴 것이다. 
   !완전 꿀팁! for문 단계별로 리스트에 담겨야 하는 값들을 "트리 형태"로 손으로 그려보면, 어떤식으로 for문과 재귀호출을 해야할 지 알게된다. 
4. main에서 DFS/BFS함수를 호출하는 형식도 생각해 볼 것!

! 주의 !
- DFS/BFS 함수에서 사용되는 리스트를 함수 호출해주고, pop()이 필요한 경우도 있으니 잊지 말 것

## Graph 저장 딕셔너리 vs 리스트
1. 딕셔너리로 그래프를 표현하는 경우:

딕셔너리를 사용하면 각 노드를 키로 하고 해당 노드와 연결된 노드들을 값으로 표현할 수 있습니다. 이 때 연결 정보를 O(1) 시간 안에 가져올 수 있어서, 특정 노드와 연결된 모든 노드들을 빠르게 탐색할 수 있습니다.
다만, 그래프의 크기가 상대적으로 작을 때 유용하며, 간선의 정보를 저장하기 위해 불필요한 공간을 사용할 수 있습니다.

2. 리스트로 그래프를 표현하는 경우:

리스트로 그래프를 표현하면 그래프의 크기에 따라 메모리 사용이 효율적입니다. 노드와 간선 정보를 따로 리스트로 관리할 수 있습니다.
연결 정보를 가져오는 과정이 딕셔너리에 비해 느릴 수 있습니다(O(N) 시간이 소요될 수 있음).
그래프의 크기가 크거나 간선 정보가 상대적으로 적을 때 유용할 수 있습니다.