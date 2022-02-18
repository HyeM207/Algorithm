-- 코드를 입력하세요
SELECT SUBSTRING(DATETIME,12,2) as HOUR, COUNT(DATETIME) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    HAVING HOUR > 8 AND HOUR <20
    ORDER BY HOUR;

/*
    - SUBSTRING(칼럼 명, 자르는 시작 위치, n개의 자르는 문자 ) : SQL에서 문자열 추출
    
    - AS : 칼럼명을 다른 이름으로 재정의할 때 사용
*/