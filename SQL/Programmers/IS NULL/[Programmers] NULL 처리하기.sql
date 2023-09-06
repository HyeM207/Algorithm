-- 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문
-- 단, 이름이 없는 동물의 이름은 "No name" 으로 표시한다.
SELECT ANIMAL_TYPE, IF(NAME IS NULL, 'No name', NAME), SEX_UPON_INTAKE
    FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID;

/*
    - IF (조건, 참, 거짓) : SQL의 조건문
*/