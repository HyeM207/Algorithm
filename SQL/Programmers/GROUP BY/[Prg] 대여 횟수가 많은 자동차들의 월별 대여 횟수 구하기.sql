-- 23.05.28 성공 
/*
이중 쿼리 문제 
- 메인 쿼리와 서브 쿼리에 모두 기간 필터링을 해줘야 됐던 문제 
- 헤맸던 부분 : 
    - 이중 쿼리 적용하지 않은 점 
        - 이중 쿼리도 FROM이 아닌 WHERE에 적용해야됨
    - 메인 쿼리에 기간 필터링 하지 않은 점 
        - 필요 이유 :  특정 car_id가 7월과 8월 9월에 모두 있다면, 메인에서 COUNT할때 7월것을 제외해야하므로, 둘다 적용해야됨
*/

-- 1차 시도 (실패)
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
GROUP BY MONTH, CAR_ID
HAVING COUNT(CAR_ID) >= 5
ORDER BY MONTH ASC, CAR_ID DESC;
-- 잘못된 점 : 문제 파악 못함, 이중 쿼리 사용 안 함 

-- 2차 시도 (실패)
SELECT 
    MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS 
FROM (
    SELECT * 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31'
    GROUP BY CAR_ID     
    HAVING count(*) >= 5
) as A
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC;
-- 잘못된 점 : car_id가 2인게 8월만 출력됨 -> 이중 쿼리를 from이 아닌 where 절에 써야됨 


-- 3차 시도 (실패)
SELECT 
    MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31'
    GROUP BY CAR_ID     
    HAVING count(1) >= 5
) 
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC;
-- 잘못된 점 : 메인 쿼리에서 한 번 더 START_DATE으로 필터링 걸어야됨 (이유: 이중 쿼리가 FROM이 아닌 WHERE절에 걸려있기에, FROM을 테이블의 모든 데이터로 지정했으니, 메인 쿼리에서 한 번더 필터링 걸어야됨 
-- 그리고 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해야됨

-- 4차 시도 (성공)
SELECT 
    MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31'
    GROUP BY CAR_ID     
    HAVING count(1) >= 5
) AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH, CAR_ID
HAVING COUNT(*) > 0
ORDER BY MONTH, CAR_ID DESC;