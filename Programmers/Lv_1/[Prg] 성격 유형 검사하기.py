
"""
2022 KAKAO TECH INTERNSHIP
"""
def solution(survey, choices):
    types = [['R','T'], ['C','F'], ['J','M'], ['A','N'] ]
    total = {
        'R': 0,
        'T': 0 ,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    score = {1:3 , 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    for i, choice in enumerate(choices):
        if choice <= 3:
            total[survey[i][0]] += score[choice]
        elif choice >= 5:
            total[survey[i][1]] += score[choice]
        
    answer = ''
    for _type in types:
        if total[_type[0]] > total[_type[1]]:
            answer += _type[0]
        elif total[_type[0]] < total[_type[1]] : 
            answer += _type[1]
        else: 
            answer += _type[0]
    return answer