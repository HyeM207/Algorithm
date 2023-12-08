# LEFT OUTER JOIN과 GROUP BY 그리고 SUM 의 조합을 이용한 풀이
# 놓친 부분: e.experience_years가 NULL인 경우, 제외해줘야됨 
SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(e.employee_id), 2) as average_years 
FROM Project p
LEFT JOIN Employee e 
ON e.experience_years is NOT NULL AND p.employee_id = e.employee_id 
GROUP BY p.project_id;