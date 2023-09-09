# So EASY 몸풀기용
def solution(name, yearning, photo):
    answer = []
    name_yearning = {}
    for i, n in enumerate(name):
        name_yearning[n] = yearning[i]
    for p in photo:
        result = 0
        for person in p:
            result += name_yearning.get(person,0)
        answer.append(result)
    return answer
