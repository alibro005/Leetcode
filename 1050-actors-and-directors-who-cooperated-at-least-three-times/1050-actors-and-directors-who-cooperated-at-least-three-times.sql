# Write your MySQL query statement below

SELECT actor_id , director_id
FROM ActorDirector
Group by actor_id , director_id
HAVING COUNT(timestamp) >= 3;