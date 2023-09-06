## Binary Search
### 원리
이진 탐색은 다음 원리만 기억하면 된다.
<B> left, right 투 포인터의 중간 값이인 mid를 target과 비교해가며 left와 right 포인터를 조정해가며 탐색 (탐색 범위를 좁혀감) </b>

### binary 모듈
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None) : a 배열에서 이진분할로 x 찾아서 해당 인덱스를 return 하는 모듈 (target이 없을 경우 return -1)