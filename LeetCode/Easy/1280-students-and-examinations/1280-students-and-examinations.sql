# 풀이 1: 서브쿼리 이용
# ! NULLIF가 아니라 IFNULL이다
# ! CROSS JOIN 활용 알아두기
# SELECT s.student_id, s.student_name, s.subject_name, IFNULL(exam_cnt.attended_exams, 0) as attended_exams
# FROM (
#     SELECT * FROM Students CROSS JOIN Subjects
#     ) s
# LEFT JOIN (
#     SELECT e.student_id, e.subject_name, COUNT(subject_name) as attended_exams
#     FROM Examinations e
#     GROUP BY e.student_id, e.subject_name) exam_cnt
# ON exam_cnt.student_id = s.student_id and exam_cnt.subject_name = s.subject_name
# ORDER BY s.student_id, s.subject_name;

# 풀이 2: 서브쿼리 없이 JOIN 2번 
# ! SELECT 할 때, e.subject_name 이 아닌 sub.subject_name 출력하기
# ! GROUP BY 할 때 subject_name을 e가 아닌 sub 테이블것으로 바꿔주기
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) as attended_exams
FROM Students s
    CROSS JOIN Subjects sub
    LEFT JOIN Examinations e
    ON e.student_id = s.student_id and sub.subject_name = e.subject_name
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id, sub.subject_name;