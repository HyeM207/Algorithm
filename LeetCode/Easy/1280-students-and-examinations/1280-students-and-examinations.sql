SELECT s.student_id, s.student_name, s.subject_name, IFNULL(exam_cnt.attended_exams, 0) as attended_exams
FROM (
    SELECT * FROM Students CROSS JOIN Subjects
    ) s
LEFT JOIN (
    SELECT e.student_id, e.subject_name, COUNT(subject_name) as attended_exams
    FROM Examinations e
    GROUP BY e.student_id, e.subject_name) exam_cnt
ON exam_cnt.student_id = s.student_id and exam_cnt.subject_name = s.subject_name
ORDER BY s.student_id, s.subject_name;

# ! NULLIF가 아니라 IFNULL이다
# CROSS JOIN 활용 알아두기