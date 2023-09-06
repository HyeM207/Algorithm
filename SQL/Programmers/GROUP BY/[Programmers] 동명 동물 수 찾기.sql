-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문 
-- 단 ,이름 없는 동물은 집계에서 제외/ 결과는 이름순 조회
SELECT NAME, COUNT(NAME) 
    FROM ANIMAL_INS 
    GROUP BY NAME
    HAVING COUNT(NAME) > 1
    ORDER BY NAME;

/*
    - Group By : 데이터를 원하는 그룹으로 나눔
                GROUP BY __(나누는 그룹명)__ 

    - HAVING : GROUP BY절과 같이 사용되며, 집계함수를 가지고 조건 비교할 때 사용됨
            즉, GROUP BY로 집계된 그룹 중, 원하는 조건만 '필터링' 하기 위해 사용됨 
            
    - ORDER BY는 맨 마지막에 하기
*/