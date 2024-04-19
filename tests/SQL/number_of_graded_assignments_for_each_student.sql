-- Write query to get number of graded assignments for each student:
SELECT student_id, count(student_id) as assignments_count FROM assignments where state = 'GRADED' group by student_id