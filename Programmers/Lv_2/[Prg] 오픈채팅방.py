# 문제 - lv.2
'''
# #1-230519 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 :
    - 출력해야되는 것: Enter와 Leave만  => result 배열 
    - 닉네임은 최종적으로 변경된 것만 필요함 => users 딕셔너리
'''
def solution(record):
    answer = []
    pprint ={1: "님이 들어왔습니다.", 0 : "님이 나갔습니다."}
    result = []
    users = {}
    for r in record : 
        action = r.split(" ")[0]
        uid = r.split(" ")[1]
        if action == "Enter":
            name = r.split(" ")[2]
            users[uid] = name
            result.append([1, uid])
        elif action == "Leave":
            result.append([0, uid])
        else : # change
            name = r.split(" ")[2]
            users[uid] = name
    # 출력
    for status, uid in result:
        answer.append(users[uid]+pprint[status])
        
    return answer