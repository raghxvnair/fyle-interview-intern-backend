-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(grade) AS count_of_grade_A_assignments 
FROM assignments 
WHERE grade = 'A' 
  AND teacher_id = (
    SELECT teacher_id
    FROM (
        SELECT teacher_id, COUNT(*) AS teacher_count
        FROM assignments 
        WHERE state = 'GRADED' 
        GROUP BY teacher_id
        ORDER BY teacher_count DESC 
        LIMIT 1
    ) AS max_teacher
);
