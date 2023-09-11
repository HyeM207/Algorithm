from collections import deque

def solution(priorities, location):
    answer = 1
    queue  = deque([idx, value] for idx, value in enumerate(priorities))
    max_num  = max(priorities)
    
    while queue:
        # 큰수를 찾아서 빼는 작업 하고, 뺄 때 idx 확인
        [idx, value] = queue.popleft()
        if value  == max_num:
            if idx == location:
                return answer
            answer += 1
            max_num = max(queue, key=lambda x: x[1])[1]
        else:
            queue.append([idx, value])
    return answer
