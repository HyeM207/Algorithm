# 📌 Select 
```
Select [집계함수][중복제거옵션][if문][출력형태](칼럼명) from (테이블명) where (조건)
    [ORDER BY (칼럼명) ASC/DESC] 
    [limit (개수)]
```

### ✨ 쿼리 순서
FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY


## #️⃣ 집계함수   
집계함수에서는 NULL값이 있으면 이를 무시하고 처리한다.
- COUNT(집합)
    - ex. count(id), count(*)
- SUM(집합)
- AVG(집합)
- MIN(집합)
- MAX(집합)


## #️⃣ 기타 계산 함수   
### (1) 소수점 관련 
- ROUND(값, 반올림할 소수점 N 번째 자리)
```sql
- ROUND(123.123, 0) -- 소수점 모두 반올림
- ROUND(123.123, 1) -- 소수점 첫번째자리까지 반올림 (둘째자리에서 반올림)
```
### (2) MIN, MAX
- MAX(칼럼명) : 칼럼 값 중 가장 큰 값
- MIN(칼럼명) : 칼럼 값 중 가장 작은 값 


## #️⃣ 중복제거 옵션 및 기타 
- `ALL` : (디폴트임) 중복 있는 상태로 출력
- `DISTINCT` : 중복 제거함 
- `limit N` : 출력 결과 중 상위 n개만 보여줌  

```sql
SELECT DISTINCT(price) FROM PRODUCT LIMIT 5; 
```

<br>

## #️⃣  조건문
### ✅ if문
IF (조건, 참, 거짓) : SQL의 조건문
ex.
```sql
SELECT ANIMAL_TYPE, IF(NAME IS NULL, 'No name', NAME), SEX_UPON_INTAKE
    FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID;
```

### ✅ CASE문
```sql
CASE 
    WHEN 조건1 THEN 반환값
    WHEN 조건2 THEN 반환값
    ELSE 반환값
END
```

## #️⃣ 출력 형태  
Date 형의 경우 `DATE_FORMAT(변수명, 출력형태)`으로 출력 형태 바꿀 수 있음 
- %Y : 4자리 년도
- %y : 2자리 년도
- %M : 영문 긴 월
- %m : 숫자 월(두자리)
- %c : 숫자 월(한자리)
- %b : 영문 짧은 월
- %d : 일자(두자리)
- %e : 일자(한자리)
- %W : 영문 긴 요일 이름
- %a : 영문 짧은 요일 이름 
- %l : 시간 (12시간)
- %H : 시간 (24시간)
- %i : 분
- %T : hh:mm:SS
- %r : hh:mm:ss AM,PM
- %s : 초


## #️⃣ where 조건절 
- 비교 연산자 : =, >, >= ,<, <=
- SQL 연산자 : 
    - `BETWEEN a and b` : a<= n <= b
    - `IN (list)` : 리스트 값 중 어느 하나라도 일치
    - `LIKE '비교문자열'` : 비교문자열과 형태 (DATE형도 가능)
        - ` % ` : 0개 이상 어떤 문자 
        - ` _ ` : 1개의 단일 문자 
    - `IS NULL` : NULL 인 경우
        - NULL 비교는 비교 연산자랑 비교할 수 없고, 만약 비교 연산하면 FALSE 리턴함
        - NULL은 공백이나 0이 아님

    - 논리 연산자 : AND, OR , NOT
    - 부정 비교 연산자 : 
        - !=, ^= , <>: 같지 않다
        - NOT 칼럼명 = : ~와 같지 않다
        - NOT 칼럼명 > : ~보다 크지 않다
    - 부정 SQL 연산자 : 
        - NOT BETWEEN a AND b
        - NOT IN (list)
        - IS NOT NULL


## #️⃣ ORDER BY 
    - ORDER BY 사용 시 ','로 칼럼 이어서 작성 가능. 단 앞에 작성한 칼럼 우선순위로 정렬됨 


## #️⃣ GROUP BY
- Group By : 데이터를 원하는 그룹으로 나눔. 즉, __같은 값을 가진 행끼리 하나의 그룹으로 묶음__
    `GROUP BY (나누는 그룹명) `

- `HAVING` : GROUP BY절과 같이 사용되며, 집계함수를 가지고 조건 비교할 때 사용됨
즉, GROUP BY로 집계된 그룹 중, 원하는 조건만 '필터링' 하기 위해 사용됨 
- ORDER BY는 맨 마지막에 하기


## #️⃣ JOIN
두 개 이상의 테이블/데이터베이스를 연결하여 데이터 검색하는 방법 
- 두 개 이상의 테이블의 칼럼을 서로 공유함


## #️⃣ concat
문자열 붙이기 (단위 출력시 사용)

## #️⃣ 별칭 
AS 칼럼명