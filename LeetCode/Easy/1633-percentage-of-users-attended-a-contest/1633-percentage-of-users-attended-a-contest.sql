# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(user_id )/u.total_users *100, 2) as percentage 
FROM Register 
INNER JOIN (
    SELECT COUNT(user_id) as total_users
    FROM Users
) u
GROUP BY contest_id 
ORDER BY percentage DESC, contest_id ASC;