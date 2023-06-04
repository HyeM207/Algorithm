-- 230604
-- 1차 시도 (실패) 
SELECT * 
FROM (
    SELECT CATEGORY, MAX(PRICE) as MAX_PRICE, PRODUCT_NAME
    FROM FOOD_PRODUCT 
    GROUP BY CATEGORY
) as max_product
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;

-- 2차 (실패): having 이용하는 것으로 고침
/*
Q. 메인쿼리의 where이 아닌, 서브쿼리의 having으로 바꾼 이유
A. 서브쿼리에서 group by -> 메인쿼리 Where 조회 순으로 진행이 되는데, 
선행단계에서 group by에서 미리 조건에 맞는 것만 그룹핑하면 더 효율적임.
만약 이게 아닌 뒷단(where)에서 필터링하면, 이미 모든 카테고리 항목을 갖고 있는 데이터에서 또 where이라는 필터링을 해야되므로 비효율적임 
*/
SELECT * 
FROM (
    SELECT CATEGORY, MAX(PRICE) as MAX_PRICE, PRODUCT_NAME
    FROM FOOD_PRODUCT 
    GROUP BY CATEGORY
) as max_product
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;

-- 3차 (성공) : FROM이 아닌 WHERE 절에서 서브쿼리 이용함
/*
!! 중요 !! 
Q. 왜 서브쿼리에서 MAX(PRICE)와 CATEGORY를 해야될까?
    조회하고자 하는 모든 칼럼을 서브쿼리 없이 한 번에 SELECT 문에 작성 못하나? 
A. group by로 카테고리를 묶었다면, max함수는 지정한 해당 칼럼의 max값을 가져옴.
    만약 group by와 max를 적용한 칼럼 외에 다른 칼럼을 함께 조회(select)하면 mapping이 안되어서 원하는 값을 가져오지 못함
    그렇기에 해당 문제에서는 카테고리별로 max(price)를 구한 후, 구한 값이랑 일치하는 레코드를 전체 테이블에서 필터링하여 값을 가져와야됨
*/
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) in (
    SELECT CATEGORY, MAX(PRICE) 
    FROM FOOD_PRODUCT 
    GROUP BY CATEGORY
    HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
)
ORDER BY MAX_PRICE DESC;