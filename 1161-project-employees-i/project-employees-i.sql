-- Write your PostgreSQL query statement below
select
p.project_id,
round (sum(e.experience_years)::numeric / count(p.project_id) , 2) as average_years 
from Project p
join Employee e
on p.employee_id = e.employee_id 
group by
p.project_id