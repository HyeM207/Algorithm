# 풀이 1 : INNER JOIN 이용 (1611ms)
# SELECT contest_id, ROUND(COUNT(user_id )/u.total_users *100, 2) as percentage 
# FROM Register 
# INNER JOIN (
#     SELECT COUNT(user_id) as total_users
#     FROM Users
# ) u
# GROUP BY contest_id 
# ORDER BY percentage DESC, contest_id ASC;

# 풀이 2 : 서브쿼리 이용 
SELECT contest_id, ROUND(COUNT(user_id) * 100 / (SELECT COUNT(user_id) FROM Users), 2) AS percentage
FROM Register 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;