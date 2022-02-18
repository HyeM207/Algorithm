-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문
-- 이때 결과는 시간대 순으로 정렬

SET @HOUR = -1;

SELECT (@HOUR := @HOUR +1) as HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE @HOUR = HOUR(DATETIME)) AS COUNT
    FROM ANIMAL_OUTS
    WHERE @HOUR < 23;

/*
    - 변수 선언 : SET @변수명 = 값;
    - 이미 값 할당한 변수의 값 변경 시 := 사용 
    
    ! 핵심 !  (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE @HOUR = HOUR(DATETIME)) AS COUNT
*/