# 풀이1: for문 2회 반복. 시간초과 (실패)
# result = [1, 2/3, 2/4, 3/2, 3/4, 4/2, 4/3]
# def balance(x, y):
#     if x/y in result:
#         return True
#     return False

# def solution(weights):
#     result = []
#     for i in range(len(weights)-1):
#         for j in range(i+1, len(weights)):
#             if balance(weights[i], weights[j]):
#                 result.append((weights[i], weights[j]))
#     return len(result)

# 풀이 2 : 순회는 한 번만 하도록. 아예 원소들의 분포를 파악해서 각 원소의 개수를 이용함
def solution(weights):
    result = 0
    answer = 0
    elements = {}
    # 원소 저장 
    for w in weights:
        elements[w] = elements.get(w, 0) + 1

    # 원소 (중복 없음) 조합 가능한지 확인
    for x in elements:
        x3 = x * 3
        if x3 % 2 == 0:
            result += elements[int(x)] * elements.get(int(x3 / 2), 0)
        if x3 % 4 == 0:
            result += elements[int(x)] * elements.get(int(x3 / 4), 0)
        x2 = x * 2
        if x2 % 3 == 0:
            result += elements[int(x)] * elements.get(int(x2 / 3), 0)
        if x2 % 4 == 0:
            result += elements[int(x)] * elements.get(int(x2 / 4), 0)
        x4 = x * 4
        if x4 % 3 == 0:
            result += elements[int(x)] * elements.get(int(x4 / 3), 0)
        if x4 % 2 == 0:
            result += elements[int(x)] * elements.get(int(x4 / 2), 0)

        answer += (elements[int(x)] * (elements[int(x)] - 1)) // 2  # 똑같은 값

    # result의 경우 똑같은 조합이 2쌍씩 위에서 더해졌으므로 2로 나눠줌
    return (result // 2) + answer
