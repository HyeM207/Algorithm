-- 230531
/*
새롭게 알게 된것 : 
    - GROUPBY는 MAX()까지 못한다.
    - MAX()는 top의 한 줄만 가져옴
    - WHERE () in () 문 
*/

-- 1차 실패
/*
잘못된 이유: 최대값을 뽑는 것이 아닌, 이미 GROUP BY로 묶여질 때 선택된 한 행이 선택됨.  
*/
SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES)
FROM REST_INFO
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC ;

-- 2차 성공
/*
MAX(FAVORITES) 함수가 서브쿼리 내에서 사용되어 각각의 FOOD_TYPE 그룹에서 가장 큰 FAVORITES 값을 찾음
*/
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) in (
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC ;