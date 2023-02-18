# 문제 - lv.1
'''
# #1-230218 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : index와 min 함수를 이용해 리스트에서 가장 작은 원소의 인덱스를 얻은 후, 리스트 길이에 따라 후속 처리했다.
'''

def solution(arr):
    minValIdx = arr.index(min(arr)) 
    if len(arr) != 1:
        del arr[minValIdx]
    else:
        arr[minValIdx] = -1
    return arr

'''
# 더 나은 풀이 : minValIdx = arr.index(min(arr))와 del arr[minValIdx] 하지 않고, 아래처럼 remove를 이용하여 최소값만 가지고 가능하다.
    arr.remove(min(mylist))

'''