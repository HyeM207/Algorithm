# 문제 - lv.1 
'''
# #1-230221 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 에라토스테네스의 체를 이용해 미리 소수 목록을 만들어 놓고, 주어진 수 배열의 조합들의 합을 구하여 소수인지 판별한다.
'''
import math

def solution(nums):
    # 소수 최대 합은 50,000을 넘지 않음 -> 에라토스테네스의 체를 이용하여 소수 미리 구해놓기
    n = 50000
    array = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n+1))+1) :
        if array[i] == True:
            j = 2
            while i*j <= n : 
                array[i*j] = False
                j += 1
    
    # 조합 개수 카운트
    answer = 0
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for z in range(j+1, len(nums)):
                tmp = nums[i] + nums[j] + nums[z] 
                if array[tmp] :
                    answer += 1

    return answer
