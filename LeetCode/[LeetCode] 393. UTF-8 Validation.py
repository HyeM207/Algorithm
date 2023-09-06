# Solution 1 - (내 풀이) - 실패 
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def check_bit(count : int, i : int) : 
            for c in range(count - 1) : 
                i += 1
                # print('chek : ', i, bin(data[i])[2:4])
                if bin(data[i])[2:4] != '10' :
                    # print("return False")
                    return False
            return True
    
    
        # main 문 
        i = 0 
        
        while i <= len(data) -1:
            n_bits = bin(data[i])[2:].find('0')
            
            if n_bits == 0 : 
                i += 1
                
            else : 
                count = bin(data[i])[2:n_bits+3].count('1') - 1 
                
                if check_bit(count, i) == False:
                    return False
                i += count 
        
        return True


# 풀이 : 파이썬의 bin과 문자열 슬라이스를 이용하여, UTF-8인지 구분하는 코드를 짜보았지만, bin()함수를 사용할 때 앞의 비트가 0일 경우에는 생략되서 나와 원하는대로 풀이가 잘 안됐다.


# Solution 2 - (책 풀이) 
class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        # 문자 바이트 만큼 10으로 시작 판별
        # Check 함수 : size 만큼 돌아서, 해당 비트의 앞부분이 0b10인지 확인하는 함수
        def check(size) :
            for i in range(start + 1 ,start + size + 1) : 
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        start = 0

        while start < len(data) : 
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else: 
                return False

        return True

# 책 풀이 : 비트 shift 연산자를 이용하여 앞의 비트열을 비교한 후, 이에 따라 뒤에 따라오는 바이트를 check함수로 검사하는 형태이다.