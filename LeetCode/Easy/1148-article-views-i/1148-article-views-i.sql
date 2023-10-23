# Write your MySQL query statement below
# 중복 있음 
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY 1;