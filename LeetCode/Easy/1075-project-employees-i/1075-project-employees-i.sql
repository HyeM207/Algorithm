# LEFT OUTER JOIN과 GROUP BY 그리고 SUM 의 조합을 이용한 풀이

# 풀이 1: 평균 계산시 직접 SUM과 COUNT 이용함
# 특이점: e.experience_years가 NULL인 경우, 제외해줘야됨 
# SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(e.employee_id), 2) as average_years 
# FROM Project p
# LEFT JOIN Employee e 
# ON e.experience_years is NOT NULL AND p.employee_id = e.employee_id 
# GROUP BY p.project_id;
/*
# 풀이 1 개선
# SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(e.experience_years), 2) as average_years 
# FROM Project p
# LEFT JOIN Employee e 
# ON p.employee_id = e.employee_id 
# GROUP BY p.project_id;
*/

# 풀이 2(더 나은 풀이) : AVG를 이용함
SELECT P.project_id AS project_id,  ROUND(AVG(E.experience_years), 2) AS average_years
FROM Project P LEFT JOIN Employee E
ON P.employee_id = E.employee_id
GROUP BY P.project_id;

/*
새로 알게된 점 
 - 첫번째 풀이의 경우, COUNT(e.employee_id)로 두었기때문에 experience_years가 NULL이더라도, employee_id가 NULL이 아님으로 카운트됨으로 미리 필터링으로 NULL을 제거해줘야된다.
 - 하지만, 두번째 풀이의 경우, AVG 함수에서 experience_years을 기준으로 NULL인건 자동으로 제외하기 때문에 코드가 더 간결해진다.
 - 첫번째 풀이를 개선하려면 COUNT(e.employee_id) 대신 COUNT(e.experience_years)를 쓰면 NULL 필터링 없이도 될 것 이다.
*/