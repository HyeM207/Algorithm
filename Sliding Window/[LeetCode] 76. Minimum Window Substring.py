# Solution 1 - 내 풀이 (실패(Time Limit Exceeded))
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 예외 처리
        if len(t) > len(s):
            return ""
        
        t_array = list(t)

        size = len(t)
        while size <= len(s):
            left = 0
            right = size - 1

            while right < len(s) :
                is_exist = True
                
                # print( s[left:right+1] )
                tmp = list(s[left:right+1])
                for c in t_array :
                    if c in tmp :
                        tmp.remove(c)
                        # print("tmp", tmp)
                    else :   
                        is_exist = False
                        break

                if is_exist :
                    return s[left:right+1]

                left += 1
                right += 1
            
            size += 1
        
        return ""

# 원리 : 슬라이딩 윈도우의 사이즈를 늘려가며, t의 문자가 주어진 윈도우에 있는지 확인하는 로직이다. 하지만 비효율적인 브루트포스 방식이라 time limit으로 해결하지 못하였다.
 
# Solution 2 - 책 풀이 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t) # 필요한 문자 각각의 수
        missing = len(t) # 필요한 문자의 전체 개수 
        left = start = end = 0
        # print('!START! need : ', need, ' missing : ', missing)
        
        # 오른쪽 포인터 이동 
        for right, char in enumerate(s, 1): # 1부터 시작 
            # print('right : ', right, ' char : ', char)
            missing -= need[char] > 0
            need[char] -= 1

            # print('need : ', need, ' missing : ', missing)
            # 필요 문자가 0이면 왼쪽 포인터 이동 판단 
            if missing ==0 : 
                # print("미싱 0!!")
                while left < right and need[s[left]] < 0 :
                    # print("조정 중 left ,s[left]" , left,  s[left])
                    need[s[left]] += 1 
                    left += 1
                    
                if not end or right - left <= end - start : # 원도우 크기가 더 작을 경우 
                    # print("갱신~!~!", left, right)
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
                
        return s[start:end]

# 책 풀이 : 오른쪽 포인터를 for문으로 돌다가, 슬라이딩 안에 필요한 문자열이 다 포함되어 있다면, left 포인터를 조정하여 길이를 줄일 수 있는 지 확인한다.
