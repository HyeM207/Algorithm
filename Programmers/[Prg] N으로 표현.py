## 문제 - lv.3
'''
# #1-230414 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 강의 보고 DP문제이고 N을 x번 사용해서 만들 수 있는 수들을 이용하여 수식을 만드는 것이 포인트라는 것을 알게되었다.
            또한  n => (1~ n-1로 만든 수)  +-/* (n-1 ~ 1로 만든 수) 인것을 활용하여 코드를 짰다.
    상세 설명 : 
        1. while문을 돌며 N을 사용하는 횟수를 관리한다.
        2. for i in range(1, x) 를 이용하여 조합을 만든다. 
            - 이때 이중 for문을 돌며 (x로 만든 수) +-/* (x-i로 만든 수) 계산한다.
'''
def solution(N, number):
    s= [ set() for _ in range(10)]
    x = 1 # N을 사용하는 횟수
    
    while x < 9 :  
        tmp = int(str(N) * x)
        if tmp == number : 
               return x 
        s[x].add(tmp)
        
        for i in range(1, x) : # 조합의 개수 
            # (x로 만든 수) +-/* (x-i로 만든 수) 계산
            # print(f"s[{i}] : {s[i]} s[{x-i}] : {s[x-i]}")
            for p1 in s[i]: 
                for p2 in s[x-i] :
                    if p1 + p2 == number : 
                        return x
                    s[x].add(p1 + p2)
                    if p1 - p2 == number : 
                        return x
                    s[x].add(p1 - p2)
                    if p1 * p2 == number : 
                        return x
                    s[x].add(p1 * p2)
                    if p1!= 0 and p2 != 0 : # zerodivision 에러 방지
                        if p1// p2 == number : 
                            return x
                        s[x].add(p1 // p2)
        x += 1   
    
    return -1