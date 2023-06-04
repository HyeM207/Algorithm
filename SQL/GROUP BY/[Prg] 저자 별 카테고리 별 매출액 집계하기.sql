-- 230604 (성공) : 오랜만에 한 번에 성공한 문제
/*
[ 구상 흐름 ]
1. BOOK_SALES 에서 해당 기간 필터링 -> book_id groupby하고 sum(SALES)
2. 1번에서 나온 정보를 Book 테이블이랑 join해서 TOTAL_SALES 구함
3. 이때 저자 별, 카테고리 별로 진행, 동시에 TOTAL_SALES 합산
4. 마지막으로 저자 이름을 위해 AUTHOR 에서 정보 가져오기
*/
SELECT 
    B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SUM_SALES*B.PRICE) as TOTAL_SALES
FROM BOOK as B 
INNER JOIN (
        SELECT BOOK_ID, SUM(SALES) as SUM_SALES
        FROM BOOK_SALES 
        WHERE LEFT(SALES_DATE, 7) = '2022-01'
        GROUP BY BOOK_ID
) as S ON B.BOOK_ID = S.BOOK_ID
INNER JOIN AUTHOR as A ON B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY B.AUTHOR_ID ASC, B.CATEGORY DESC;
