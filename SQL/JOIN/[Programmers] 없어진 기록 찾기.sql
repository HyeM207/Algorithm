-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME 
    FROM ANIMAL_INS RIGHT JOIN ANIMAL_OUTS
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    WHERE ANIMAL_INS.ANIMAL_ID IS NULL;


/*
    [JOIN]
    ex. 집합 A (왼쪽), 집합 B(오른쪽) (교집합 존재 가정)

    - 교집합 : FROM A INNER JOIN B 
                ON A.ID = B.ID;

    - (JOIN기준 왼쪽 부분) 교집합 + 집합 A 
            : FROM A LEFT OUTER JOIN B
            ON A.ID = B.ID;

    - 집합 A에서 교집합 제거 
            : FROM A LEFT OUTER JOIN B
            ON A.ID = B.ID
            WHERE B.ID IS NULL;

    - (JOIN기준 오른쪽 부분) 교집합 + 집합 B
            : FROM A RIGHT OUTER JOIN B
            ON A.ID = B.ID;

    - 집합 B에서 교집합 제거 
            : FROM A RIGHT OUTER JOIN B
            ON A.ID = B.ID
            WHERE A.ID IS NULL;            

    - (합집합) FULL OUTER JOIN : 
            : FROM A FULL OUTER JOIN B
            ON A.ID = B.ID;

    - (합집합 - 교집합) FULL OUTER에서 교집합 제거
            : FROM A FULL OUTER JOIN B
            ON A.ID = B.ID
            WHERE A.ID IS NULL OF B.ID IS NULL;  

*/