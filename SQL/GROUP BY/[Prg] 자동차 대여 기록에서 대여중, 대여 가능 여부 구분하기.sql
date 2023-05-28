-- 23.05.28 성공 
/*
핵심 : CAR_ID당 여러 history가 있는데, 이를 하나로 바꿔야됨
    - GROUP BY 로 car_id로 묶는데, 이때 대여중인게 있으면 1로 없으면 0으로 하여 모든 history에 대해 sum을 구함 
    -> 그리고 sum이 1이면 대여중으로, 0이면 대여가능으로 표시함
*/
SELECT CAR_ID, 
    IF(SUM(IF(START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16', 1, 0))=1, '대여중','대여 가능') AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;