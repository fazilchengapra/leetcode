-- Write your PostgreSQL query statement below
SELECT DISTINCT ON (player_id)
player_id, event_date first_login 
FROM Activity
ORDER BY player_id, event_date;