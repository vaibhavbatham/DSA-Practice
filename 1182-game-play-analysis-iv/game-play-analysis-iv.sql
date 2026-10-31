-- Write your PostgreSQL query statement below

select
Round(
    count(DISTINCT player_id)::numeric /
    (select count(DISTINCT player_id) from Activity)
,2) as fraction
from Activity
where (player_id , event_date) in (
    select 
    player_id , 
    min(event_date) + 1 
    as first_date 
from Activity
group by player_id
);
