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
- `IF (조건, 참, 거짓)` : SQL의 조건문
ex.
```sql
SELECT ANIMAL_TYPE, IF(NAME IS NULL, 'No name', NAME), SEX_UPON_INTAKE
    FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID;
```
- `IFNULL(칼럼, NULL이면 대체할 값)` : NULL인 칼럼에 출력할 값 대체
```sql
SELECT IFNULL(s.attended_exams, 0) as attended_exams
FROM Student s;
```

### ✅ CASE문
```sql
CASE 
    WHEN 조건1 THEN 반환값
    WHEN 조건2 THEN 반환값
    ELSE 반환값
END
```

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
- `INNER JOIN` : 두 테이블의 교집합
- `OUTER JOIN` : 한 테이블에만 데이터 있어도 출력
    - LEFT, RIGHT, FULL 종류 있음
    - (예시) A테이블의 특정 칼럼을 기준으로 B테이블에는 매칭되는 값이 없다면, A테이블 기준 B 테이블을 LEFT JOIN하면 A테이블의 X칼럼의 값이 NULL로 들어감
    - Mysql  에서는 `LEFT OUTER JOIN` 이 아닌 `LEFT JOIN`으로 사용한다.
- `CROSS JOIN` : 두 테이블 모두 모든 행을 조인함
- `SELF JOIN` : 자기 자신과 조인 (INNER JOIN과 동일)
![Alt text](image.png)
- 출처 : https://hongong.hanbit.co.kr/sql-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95-joininner-outer-cross-self-join/

## #️⃣ concat
문자열 붙이기 (단위 출력시 사용)

## #️⃣ 별칭 
AS 칼럼명


<hr>
<br>

# 📌 날짜 관련 함수

## #️⃣ DATE 형 출력 형태  
Date 형의 경우 `DATE_FORMAT(변수명, 출력형태)`으로 출력 형태 바꿀 수 있음 
- `%Y` : 4자리 년도
- `%y` : 2자리 년도
- `%M` : 영문 긴 월
- `%m` : 숫자 월(두자리)
- `%c` : 숫자 월(한자리)
- `%b` : 영문 짧은 월
- `%d` : 일자(두자리)
- `%e` : 일자(한자리)
- `%W` : 영문 긴 요일 이름
- `%a` : 영문 짧은 요일 이름 
- `%l` : 시간 (12시간)
- `%H` : 시간 (24시간)
- `%i` : 분
- `%T` : hh:mm:SS
- `%r` : hh:mm:ss AM,PM
- `%s` : 초

## #️⃣ 특정 년,월,시 등 추출

| 함수 | 설명 | 
| --- | ---|
| `DATE(표현식)` | 표현식에 맞는 날짜 정보 | 
| `MONTH(date)`  | 월 (0~12) |
| `DAY(date)` | 일(0~31) |
| `HOUR(DATE)` | 시간 (0~23) |
|`MINUTE(date)` | 분 (0~59)| 
| `SECOND(date)` | 초(0~59) | 
| `WEEKDAY(date)` | 요일 (월=0 ~ 일=6)| 
| `LAST_DAY(date)` | 해당 월의 마지막 날짜 | 
| `SEC_TO_TIME(seconds)`| seconds를 기준으로 시간 정보 반환(형식 HH:MM:SS)|

## #️⃣ 특정 날짜/시간 연산
### ✅ 일자 및 시간 더하고 빼기
| 함수 | 설명 | 
| --- | ---|
| `ADDDATE(date, INTERVAL value addunit)` | date에 unit단위 만큼 value를 더한 date 반환| 
| `SUBDATE(date, INTERVAL value unit)`| date에 unit단위 만큼 value를 뺀 date 반환 |
| `ADDTIEM(datetime, addtime)` | datetime에 addtime 만큼 시간을 추가한 datetime을 반환|
| `SUBTIEM(datetime, addtime)` | datetime에 addtime 만큼 시간을 뺀 datetime을 반환|

```sql
SELECT w.id
FROM Weather w
    JOIN Weather wc
    ON SUBDATE(w.recordDate, INTERVAL 1 DAY) = wc.recordDate
WHERE w.temperature > wc.temperature;
```
### ✅ 두 date 기간 차이 구하기
| 함수 | 설명 | 
| --- | ---|
| `PERIOD_DIFF(기간1, 기간2)` | 두 기간 차이 숫자로 반환 ('기간' 형식은 YYMM 혹은 YYYYMM 형식, 기간1과 기간2는 같은 형식이어야 함)|
| `DATEDIFF(date1, date2)` | 두 날짜 사이 일수 숫자로 반환 |
| `TIMEDIFF(time1, time2)` | 두 시간 차이를 datetime 타입으로 반환 |  

### ✅ 두 date 기간안에 있는지 계산하기 
- Mysql에서는 DATE 형의 값끼리 `BEWTWEEN A AND B` 구문 (단, A와 B모두 DATE형)을 사용하여 해당 기간안에 비교할 날짜가 속하는지 계산할 수 있다.
