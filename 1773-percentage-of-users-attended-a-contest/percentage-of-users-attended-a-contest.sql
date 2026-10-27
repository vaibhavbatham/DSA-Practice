-- Write your PostgreSQL query statement below
select 
r.contest_id,
round( count(r.contest_id)::numeric / (select count(*) from users) * 100 ,2) as percentage 
from Users u
right join Register r
on u.user_id = r.user_id
group by r.contest_id
order by percentage  DESC , r.contest_id ASC;