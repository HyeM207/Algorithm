-- 230530_FROM에 2개 테이블 두고, Group by 하면 해결되는 문제
SELECT 
    CATEGORY, 
    SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B, BOOK_SALES S 
WHERE B.BOOK_ID = S.BOOK_ID AND LEFT(S.SALES_DATE,7) ='2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY;