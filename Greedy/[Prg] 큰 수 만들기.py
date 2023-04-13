## 문제 - lv.2
'''
# #1-230413 실패
    정확성: 95.5
    합계: 95.5 / 100.0
    틀린 테/스트케이스 : 10 (시간초과)
    설명 : 배열로 바꿔서, front+1이 front보다 큰 경우(=오름차순 증가) 하는 경우를 인덱스 0부터 찾아서 해당 인덱스를 삭제한다.
        만약 오름차순 증가가 없었으면 맨 뒤 원소를 삭제한다. 
    추가 설명 : 원래는 테케 8,10 둘 다 시간 초과 났었는데, 
            (1) 9인지 비교하는 검사하고,
            (2) front=0초기화 하는 코드 while 문 밖으로 빼고, 
            (3) 삭제한 부분 부터 다시 검사하는 코드로 바꿨는데도 안됐다. 
'''
def solution(number, k):
    number = list(number)
    # 앞자리 보다 뒷자리가 더 크면 삭제해도 됨
    front = 0 
    while k > 0 :
        notDeleted = True
        while front < len(number) -1 :
            # 있으면 삭제, 끝까지 없으면 마지막 자리 삭제
            # 9는 시간 절약하기 위해 확인함
            if number[front] != 9 and number[front+1] > number[front] :
                del number[front]
                notDeleted = False
                k-=1
                # 삭제한 그 부분부터 다시 검사
                if front - 1 >= 0 :
                    front -= 1 
                break
            front += 1

        # 만약 오름차순 삭제가 없었으면 마지막 원소를 삭제함    
        if notDeleted :
            number.pop()
            k-=1
        
    return ''.join(number)

'''
# #2-230413 성공
    정확성: 100
    합계: 100.0 / 100.0
    설명 : (강의참고) (#1과 거의 비슷한 알고리즘) 뒤에 숫자가 더 크면 문자를 빼낸다. 이때 `collected` 스택을 사용하여 풀이함 
'''
def solution(number, k):
    collected = []
    for idx, num in enumerate(number):
        # 마지막 원소가 num보다 작으면 쌓은 문자를 빼냄 (K>0은 아직 빼낼게 있다는 뜻)
        while len(collected) > 0 and collected[-1] < num and k >0 :
            collected.pop()
            k -= 1
        if k == 0 : # 모든 작업을 했을 때
            collected += list(number[idx:])
            break
        collected.append(num)
        
    # 만약 다 안 빼냈으면 문자열 슬라이스로 k개를 뺀다
    collected = collected[:-k] if k > 0 else collected 
    return ''.join(collected)