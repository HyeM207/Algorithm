# Solution 1 -(내 풀이) - 성공
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)) : 
            j = 0 
            while j < len(matrix[i])  :
                if matrix[i][j] < target :
                    j += 1
                elif matrix[i][j] > target :
                    break
                else: 
                    return True
        return False


            
# 풀이 : 매 행을 for문으로 탐색하고 열은 white문으로 접근하여, target보다 값이 작으면 다음 열을, target보다 값이 크면 while문을 break해서 다음 행으로 넘어가도록 하였다. 


# Solution 2- 책 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 예외 처리
        if not matrix : 
            return False

        # 첫 행의 맨 뒤
        row = 0 
        col = len(matrix[0]) - 1


        while row <= len(matrix) - 1 and col >= 0 :
            if target == matrix[row][col] :
                return True
            elif target < matrix[row][col] :
                col -= 
            elif target > matrix[row][col] :
                row += 1

        return False
# 풀이 : 책의 풀이 방식은 '첫 행의 맨 뒤'에서 부터 접근하여 탐색하는 방식을 사용하였다. 
#       행의 맨 뒤에서 부터 접근하면, 작으면 왼쪽으로, 크면 아래쪽으로 이동하면 되기때문에 위의 방식을 이용한 것을 보인다. 
                 
            


# Solution 3 - 책 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        return any(target in row for row in matrix)

# 풀이 : 위 풀이는 for문으로 행을 접근하여 in으로 값의 존재 여부를 확인하는 코드이다.

#       any () : 포함된 값 중 어느 하나가 참이라면 항상 참으로 출력함
#       all () : 모든 값이 참이어야 True 출력함
