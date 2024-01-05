# 풀이 1 (240105) : 성공
def solution(picks, minerals):
    """
    5개씩 묶어서 3가지 곡갱이로 처리했을때 피로도를 모두 구한 후, 
    피로도가 높은 순서대로 좋은 곡갱이를 할당한다.
    
    (* minerals의 길이가 최대 50이기에, 피로도 모두 구해도 괜찮음)
    ! 놓친 부분 : 테케8. 곡괭이 수가 광물의 집합보다 작은 경우 ! 
    """
    answer = 0
    fatigue = {'diamond' : [1,5,25], 'iron' : [1,1,5], 'stone' : [1,1,1]} # key : 채굴할 광물 / value : [dia, iron, stone] 별 피로도
    fatigue_per_five = []
    
    # 과정 1 : 5개씩 묶어서 돌 곡갱이로 처리했을때 피로도를 구함
    # 주의. 곡괭이 수가 광물의 집합보다 작은 경우, 곡갱이 수만큼만 배열 원소 처리함
    n = sum(picks)*5 if sum(picks)*5 < len(minerals) else len(minerals) 

    for i in range(0, n, 5):
        dia_hap, iron_hap, stone_hap = 0, 0, 0
        for j in range(i, i+5):  
            if j >= n:
                break
            dia_hap += fatigue[minerals[j]][0]
            iron_hap += fatigue[minerals[j]][1]
            stone_hap += fatigue[minerals[j]][2]
        fatigue_per_five.append([dia_hap, iron_hap, stone_hap])
    
    # 과정 2 : 돌 곡갱이 기준 피로도가 높은 순서대로 정렬 후, 순서대로 좋은 곡갱이를 할당한다.
    fatigue_per_five.sort(key=lambda x: (x[2], x[1]), reverse=True)
    idx_five = 0
    for pick_idx, tool_cnt in enumerate(picks):
        for j in range(tool_cnt):
            if idx_five >= len(fatigue_per_five):
                break
            answer += fatigue_per_five[idx_five][pick_idx] 
            idx_five += 1
            
    return answer