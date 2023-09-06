# Solution 1 (내 풀이)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2 = list(set(nums2))        
        result = []

        for target in nums2:
            left, right =0, len(nums1) -1
            while left <= right :
                mid = (left + right) // 2
        
                if nums1[mid] < target : 
                    left = mid + 1
                elif nums1[mid] > target : 
                    right = mid - 1
                else : 
                    if nums1[mid] == target :
                        result.append(target)
                    break
            
        return list(set(result))
        
# 풀이 : 이진 탐색 기법을 이용하였다.  중복없이 이루어진 nums2의 원소가 정렬된 num1을 이진탐색하면서 해당 원소가 있다면 결과 리스트에 append하는 흐름이다. 

# Solution 2 (책 풀이)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ressult: Set = set()
        nums2.sort()        

        for n1 in nums1 : 
            i2 = bisect.bisect_left(num2,n1) # num2에서 n1값의 인덱스 값 리턴

            if len(num2) > 0 and len(num2) > i2 and n1 == num2[i2]
                result.add(n1)
        
        return result
        

# 풀이 : 해당 풀이는 파이썬에서 제공하는 이진 탐색 함수를 이용하여 푼 풀이로, 정렬해둔 num2에서 num1의 원소가 있는지 확인 후 result 집합에 add하는 흐름이다.

#  bisect.bisect_left(a, b) : a배열에서 b의 타겟을 찾아서 해당 인덱스를 return 하는 모듈