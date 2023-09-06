-- 230530
/* 1차 풀이 통과 - but 비효율적. FROM 2개로 조회하는 쿼리를 서브 쿼리로 두고, 메인 쿼리에서 70만원 이상인 것만 출력함  */
SELECT * FROM (
    SELECT
        users.USER_ID,
        users.NICKNAME,
        sum(board.PRICE) as TOTAL_SALES
    FROM USED_GOODS_BOARD board, USED_GOODS_USER users
    WHERE board.WRITER_ID=users.USER_ID AND board.STATUS='DONE'
    GROUP BY users.USER_ID
) as B WHERE TOTAL_SALES >=700000
ORDER BY TOTAL_SALES

/*2차 풀이 통과 - 이중 쿼리없이 HAVNIG으로 바꿈 */
SELECT
    users.USER_ID,
    users.NICKNAME,
    sum(board.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD board, USED_GOODS_USER users
WHERE board.WRITER_ID=users.USER_ID AND board.STATUS='DONE'
GROUP BY users.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES;

/* 3차 통과-효율적 쿼리 */
-- join이용해서 테이블 하나만 FROM에 쓰고, HAVING절을 이용하여 합계 조건 달리함
SELECT
    users.USER_ID,
    users.NICKNAME,
    SUM(board.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD board
JOIN USED_GOODS_USER users ON board.WRITER_ID = users.USER_ID
WHERE board.STATUS = 'DONE'
GROUP BY users.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES;