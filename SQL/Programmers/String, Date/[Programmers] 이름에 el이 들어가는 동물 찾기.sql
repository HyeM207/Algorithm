-- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문
-- 이때 결과는 이름 순으로 조회
SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS 
    WHERE NAME LIKE '%el%' and ANIMAL_TYPE = 'Dog'
    ORDER BY NAME; 