-- Write your PostgreSQL query statement below
select
query_name, 
round(AVG (rating :: numeric / position) , 2) as quality,
round(
    AVG(case 
    when rating < 3 
    then 1.0
    else 0.0 end ) *100
    ,2) as poor_query_percentage 

from Queries
group by query_name 