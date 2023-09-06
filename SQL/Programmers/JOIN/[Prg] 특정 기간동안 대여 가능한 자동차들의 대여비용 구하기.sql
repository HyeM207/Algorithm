-- 230612 성공
/*
- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능 -> WHERE의 NOT IN 사용
- 종류 ('세단', 'SUV') -> WHERE
- 할인율 매칭 -> CROSS JOIN
    - CROSS JOIN 사용한 이유: 해당되는 할인율이 여러개 일 수 있으므로 CROSS JOIN함
- 30일간의 대여 금액이 50만원 이상 200만원 미만  -> HAVING


!! HAVING !!
- 보통 HAVING은 GROUP BY와 함께 쓰이지만, 
 집계 또는 계산된 값에 적용된 조건을 기준으로 "행을 필터링"하는 데 사용될 수 있다. 
-  HAVING 절은 SELECT, FROM, WHERE 절이 처리된 후 결과 집합을 필터링하는 데 적용됨
*/
SELECT car.CAR_ID, car.CAR_TYPE,
        ROUND(30*car.daily_fee*(100-discount.discount_rate)/100) as FEE
FROM CAR_RENTAL_COMPANY_CAR as car 
CROSS JOIN (
    SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    WHERE CAR_TYPE IN ('세단', 'SUV') AND DURATION_TYPE='30일 이상'
) as discount
ON car.CAR_TYPE	= discount.CAR_TYPE	
WHERE car.CAR_TYPE IN ('세단', 'SUV') 
    AND CAR_ID NOT IN (
    SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  
    WHERE '2022-11' BETWEEN LEFT(START_DATE,7) AND LEFT(END_DATE, 7) ) 
HAVING FEE BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, car.CAR_TYPE ASC, car.CAR_ID DESC;