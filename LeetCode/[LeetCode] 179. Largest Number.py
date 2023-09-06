# Solution1 - (책 풀이)

class Solution:
    
    @staticmethod   
    #staticmethod : 정적 메소드로  인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 메서드
    def to_swap(n1: int, n2: int) -> int:
        return str(n1) + str(n2) < str(n2) + str(n1) #문자열을 더하여 앞 자리부터 크기 비교 가능함
    
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        
        while i < len(nums):
            j = i 
            while j > 0 and self.to_swap(nums[j-1], nums[j]) :
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1   
            i+= 1

        return str(int(''.join(map(str, nums))))


# 후기 : 처음에 혼자 풀어보려고 2,1,0인 경우에 따라 원소 위치를 변경하고 포인터 인덱스를 바꾸는 방법을 생각했는데, 풀다보니 예외 경우가 너무 많아 해당 풀이는 버렸다.  
# 책 풀이 : 위 풀이는 삽입 정렬과 문자열로 두 수를 합쳐 크기 비교하는 방식을 이용한 풀이이다. 
#             [ 삽입 정렬 ]
#               - j-1의 값과 j번째의 값을 비교하여 뒤의 값이 크다면 둘의 위치를 변경한다. 
#               - i는 첫번째 인덱스부터 마지막 인덱스까지 이동하는 포인터고, j는 i 포인터로 하여 nums[j]의 값이 크면 리스트 앞쪽으로 이동한다. (while문)  