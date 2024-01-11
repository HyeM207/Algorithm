# 풀이 1 (240111) : 성공 - 코드 별로임
from collections import Counter
from itertools import combinations
import re

def solution(user_id, banned_id):
    def get_restrict_id(b_id):
        """정규표현식 이용하여 찾기"""
        pattern = re.sub(r'\*', '.', b_id)
        pattern = f'^{pattern}$'
        p = re.compile(pattern)
        
        restrict = []
        for uid in user_id:
            if p.match(uid):
                restrict.append(uid)
                
        return restrict
    
    def search(i, matches=[]):
        """
        가능한 쌍을 모두 구함 => 이때 banned_id 중복쌍도 고려하여 처리함
        """
        nonlocal answer  # nonlocal 키워드를 사용하여 외부 함수의 변수를 참조
        if i >= len(banned_counter_key):
            if len(matches) == len(banned_id):
                answer.append(tuple(sorted(matches)))  # 중복된 조합을 고려하여 정렬 후 tuple로 추가
            return 
        b_id = banned_counter_key[i]
    
        # (1). 기존에 사용하지 않은 r_id 구함
        poss_r_id = []
        for r_id in restrict_id[b_id]:
            if r_id not in matches:
                poss_r_id.append(r_id)
                
        # (2). b_id가 중복된 쌍이라면 가능한 r_id 조합 구해줌
        r_id_combi = list(combinations(poss_r_id, banned_counter[b_id]))
        for r_ids in r_id_combi:
            search(i+1, matches+list(r_ids))
    
    # 1. 중복없앤 banned_id와 user_id 매칭되는 리스트 만들기
    restrict_id = {}
    for b_id in set(banned_id):
        r_id = get_restrict_id(b_id)
        if len(r_id) == 0:
            return 0
        restrict_id[b_id] = r_id
    
    # 2. 가능한 제재 아이디 목록을 구한다
    banned_counter = Counter(banned_id)
    banned_counter_key = list(banned_counter.keys())
    answer = []
    search(0)
    
    # 중복을 제거하고 최종 결과의 개수를 반환
    return len(set(answer))


# 풀이 2 (240111) : 성공 - 풀이 1 개선
"""
counter 사용하지 않고, banned_id 리스트를 그대로 순회하며 가능한 restrit_id를 matches에 append함
 - counter 필요 없는 이유 : answer에서 set으로 중복 처리하기 때문에, 중복되는 banned_id를 신경 쓸 필요없다.
"""
from collections import Counter
import re

def solution(user_id, banned_id):
    def get_restrict_id(b_id):
        """정규표현식 이용하여 찾기"""
        pattern = re.sub(r'\*', '.', b_id)
        pattern = f'^{pattern}$'
        p = re.compile(pattern)
        
        return [uid for uid in user_id if p.match(uid)]
    
    def search(i, matches=[]):
        nonlocal answer  
        if i >= len(banned_id):
            answer.add(tuple(sorted(matches)))  
            return 
        
        b_id = banned_id[i]
        poss_r_id = get_restrict_id(b_id)
        
        for r_id in poss_r_id:
            if r_id not in matches:
                search(i+1, matches + [r_id])
    
    answer = set()
    search(0)

    return len(answer)
