-- Write your PostgreSQL query statement below
select
to_char(trans_date ,'YYYY-MM')  as month,
country,
count(*) as trans_count,
count(*) filter(where state = 'approved') as approved_count ,
coalesce (sum(amount), 0) as trans_total_amount ,
coalesce (SUM(amount) FILTER (where state  = 'approved'), 0)as approved_total_amount 
from Transactions
group by 
TO_CHAR(trans_date, 'YYYY-MM'),
country ;