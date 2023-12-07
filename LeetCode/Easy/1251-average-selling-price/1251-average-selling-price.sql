/*
 - 총 가격과 총 판매 개수가 필요함
 - 헷갈린 부분: GROUP BY 와 SUM  부분 계산 순서때문에 어떻게 쿼리를 짜야될지 헷갈렸음
 - 새로 알게된 것 : MySQL에서 DATE형의 기간 간격 계산은 BETWEEN 으로 가능하다
 - 놓친 부분 : LEFT INNER JOIN 이 아닌 LEFT OUTER JOIN 을 해야된다. 이때 NULL처리는 IFNULL 이용하기
*/
SELECT p.product_id,  IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units), 2), 0) as average_price 
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id and u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;