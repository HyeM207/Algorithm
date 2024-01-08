# 풀이 1 (240108) : 성공
def solution(msg):
    """
    주어진 알고리즘 순서대로 구현함
    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w과 다음 글자 c를 찾는다.
    # 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
    # 4. 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
    """
    answer = []
    n = len(msg)
    w_dict = {}
  
    for char in range(ord('A'), ord('Z') + 1):
        w_dict[chr(char)] = char - ord('A') + 1
    w_new_idx = len(w_dict) + 1
    
    i = 0 
    while i < n:
        w = msg[i]
        last_i = i
        while last_i < n and msg[i:last_i + 1] in w_dict:
            last_i += 1
        w = msg[i:last_i]
        c = msg[last_i] if last_i < n else ''  
        answer.append(w_dict[w])
        if c:
            w_dict[w+c] = w_new_idx
            w_new_idx += 1
        i = last_i 
        
    return answer
