# 풀이 1 : INNER JOIN 이용 (1611ms)
SELECT contest_id, ROUND(COUNT(user_id )/u.total_users *100, 2) as percentage 
FROM Register 
INNER JOIN (
    SELECT COUNT(user_id) as total_users
    FROM Users
) u
GROUP BY contest_id 
ORDER BY percentage DESC, contest_id ASC;

# 풀이 2 : 서브쿼리 이용 (1975ms)
# SELECT contest_id, ROUND(COUNT(user_id) * 100 / (SELECT COUNT(user_id) FROM Users), 2) AS percentage
# FROM Register 
# GROUP BY contest_id
# ORDER BY percentage DESC, contest_id;

/*
==> 풀이 1 INNER JOIN이 더 나은 풀이임
- MySQL 5.5에서는 서브쿼리 최적화가 많은 문제를 갖고 있음. 5.6부터 개선되었긴 하지만,
 버전/조건 관계 없이 좋은 성능을 내려면 최대한 Join을 이용하자
 
 참고 : https://jojoldu.tistory.com/520
*/