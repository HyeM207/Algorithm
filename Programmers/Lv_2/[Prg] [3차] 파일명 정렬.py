import re
def solution(files):
    splited = [] # [ [본 문자, head, number, 원래 순서], ... ]
    for idx, file in enumerate(files):
        j = 0  
        # number 부분 찾기
        while j < len(file):
            if file[j].isdigit():
                check = j
                while check < len(file):
                    if file[check].isdigit():
                        check+=1
                    else:
                        break
                break
            j += 1
        splited.append([file, file[:j], file[j:check], idx])
    splited.sort(key= lambda x: (
            x[1].upper(),
            int(x[2]),
            int(x[3])
    ))
    return [ x[0] for x in splited]
