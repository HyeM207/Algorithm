-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문
-- 이때 결과는 보호 기간이 긴 순으로 조회
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
    FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS 
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    ORDER BY  DATEDIFF(ANIMAL_OUTS.DATETIME,ANIMAL_INS.DATETIME) DESC LIMIT 2;


/*
    - DATEDIFF(expr1, expr2) : expr1 - expr2의 날짜 차이를 계산함
        expr1, expr2의 타입은 DATETIME 등 날짜 형태이어야 한다.
*/