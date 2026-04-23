-- Write your PostgreSQL query statement below
delete from Person p where exists (select 1 from Person p2 where p.email = p2.email and p.id > p2.id)