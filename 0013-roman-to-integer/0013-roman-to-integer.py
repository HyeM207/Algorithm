class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        roman_four = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        answer = 0
        prev = s[0]
        answer += roman.get(prev, 0)
        for c in s[1:]:
            print(prev+c)
            if prev+c in roman_four.keys():
                answer -= roman.get(prev, 0)
                answer += roman_four.get(prev+c, 0)
                
            else:
                answer += roman.get(c, 0)
            prev=c
        return answer