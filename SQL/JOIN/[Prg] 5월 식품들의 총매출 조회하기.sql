-- 230611 성공
SELECT 
    f_order.PRODUCT_ID, 
    product.PRODUCT_NAME, 
    SUM(product.price * f_order.AMOUNT)
FROM FOOD_ORDER as f_order INNER JOIN FOOD_PRODUCT as product
ON f_order.PRODUCT_ID = product.PRODUCT_ID
WHERE LEFT(f_order.PRODUCE_DATE, 7)='2022-05' 
GROUP BY f_order.PRODUCT_ID
ORDER BY 3 desc, 1 asc;