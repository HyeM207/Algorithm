# Write your MySQL query statement below
SELECT w.id
FROM Weather w
    JOIN Weather wc
    ON SUBDATE(w.recordDate, INTERVAL 1 DAY) = wc.recordDate
WHERE w.temperature > wc.temperature;