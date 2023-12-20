class Solution:
    def intToRoman(self, num: int) -> str:
        """
        풀이 1: 자리수대로 접근 => 이때 4,9는 필터링 => 남은 수에 대해 5이상과 미만으로 나눠서 처리
        =>  O(1)
        """
        symbols = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
           4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        
        answer = ''
        l = len(str(num))
        for i, n in enumerate(str(num)):
            tens = 10 ** (l-i-1)
            if int(n)*tens in symbols:
                answer += symbols[int(n)*tens ]
            else:
                if int(n) >= 5:
                    answer += symbols[5*tens] + symbols[tens] * (int(n)-5)
                else:
                    answer += symbols[tens] * int(n)

        return answer