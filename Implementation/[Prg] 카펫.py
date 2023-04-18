# 문제 - lv.2
'''
# #1-230418 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 가로 x, y에 대한 xy와 x+y값을 구한 후, xy 곱의 최대 공약수를 구해 그 합이 x+y가 되는 수를 찾아 return한다. (lv은 1같았다.)
'''
def solution(brown, red):
    answer = []
    # 가로가 x, 세로가 y일 경우
    # brown = 2x + 2(y-2) = 2(x+y) - 4 => x+y = (brown + 4)/2
    # red = (x-2)(y-2) = xy -2(x+y) + 4 => xy = red-4 + 2(x+y)
    hap = int((brown + 4)/2)
    xy = int((red-4)+2*hap)
    
    # x,y에 대해 합과 곱을 알았으니 곱을 이용해, 최대 공약수를 구해 합과 일치하는 x,y를 찾는다.
    for i in range(1, xy//2+1):
        if xy%i == 0: 
            x = xy//i
            y = i
            if x + y == hap : 
                answer = [x,y]
                break

    answer.sort(reverse=True)
    return answer