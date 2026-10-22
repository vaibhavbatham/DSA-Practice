-- Write your PostgreSQL query statement below
    select 
    st.student_id ,
    st.student_name ,
    sub.subject_name,
    count(ex.subject_name) as attended_exams 
    from Students st
    CROSS JOIN Subjects sub
    left join Examinations ex
    on st.student_id = ex.student_id
    AND sub.subject_name = ex.subject_name
    GROUP BY
    st.student_id,
    st.student_name,
    sub.subject_name
    ORDER BY
    st.student_id,
    sub.subject_name;

