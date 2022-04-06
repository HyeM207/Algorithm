# Solution 1 - (내 풀이) -실패
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0과 2만 정렬하자
        
        p = 0
        while p < len(nums)  :
            print("p: ", p, "nums[p] :", nums[p])
            if nums[p] == 1 : 
                p += 1
                print('!', nums)
            elif nums[p] == 2 :
                nums.append(nums.pop(p)) # p번째 원소 pop하여 nums 맨 뒤에 붙이기
                print("@", nums)
            elif nums[p] == 0 :
                nums.insert(0, nums.pop(p))
                p += 1
                print("#", nums)
        print(nums)

# 풀이 : 삽입 정렬 알고리즘은 이전에 전공 수업 때 배워서 어렴풋이 기억은 했지만, 어떤 식으로 구현해야될 지 감이 잡히지 않아 책 풀이를 참고하였다.


# Solution 2 - (책 풀이)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue :
            if nums[white] < 1: # 1. 0인 경우
                nums[red], nums[white] = nums[white], nums[red] # swap
                white += 1
                red += 1
            
            elif nums[white] > 1: # 2. 2인 경우
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white] # swap
            
            else:   # 3. 1인 경우 
                white += 1

# 풀이 : 각각 0,1,2 부분의 인덱스를 가르키는 red, white, blue 포인터를 두고,
#        white로 인덱스를 처음부터 끝까지 이동하며 값에 따라 swap하는 구조이다.
#       [ nums[white]이 n일 경우 ]
#           n = 1  : white 포인터 +1 이동
#           n = 2 : white 포인터와 blue 포인터가 가르키는 값을 swap & 포인터 위치 조정
#           n = 0 : white 포인터와 red 포인터가 가르키는 값을 swap & 포인터 위치 조정

# 후기 : 다익스트라가 제안한 '네덜란드 국기 문제'와 동일한 문제라고 한다. 그리 어렵지 않으면서 재미있는 문제였다! 