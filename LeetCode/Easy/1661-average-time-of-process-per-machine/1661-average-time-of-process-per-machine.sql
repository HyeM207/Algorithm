# Write your MySQL query statement below
SELECT t.machine_id, ROUND(AVG(processing_time), 3) as processing_time
FROM (
        SELECT p.machine_id, p.process_id, SUM(pc.timestamp - p.timestamp) as processing_time
        FROM Activity p 
            JOIN Activity pc
            ON p.process_id = pc.process_id and p.machine_id = pc.machine_id and pc.activity_type = 'end' 
        GROUP BY p.machine_id, p.process_id
    )t
GROUP BY t.machine_id;