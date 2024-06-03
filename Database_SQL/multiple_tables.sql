-- 607 sales person
-- # Write your MySQL query statement below
-- -- select s.name as name
-- -- from salesperson as s 
-- -- left join orders as o on o.sales_id = s.sales_id
-- -- left join company as c on c.com_id = o.com_id 
-- -- group by s.sales_id 
-- -- having sum(case when c.name='RED' then 1 else 0 end) = 0

-- method wrong: this is the over complex, use to understand multiple tables. For right solution, jump to next method directly
with only_in_order as 
(
    select sp.name as name
    from orders as o 
    left join salesperson as sp 
    on sp.sales_id = o.sales_id
    left join company as cp 
    on cp.com_id = o.com_id
    where cp.name != 'RED' -- this will miss sales which deals with RED and also other companies
), 
only_in_sales as -- find the sales name which are not in order
(
select sp.name as name 
from salesperson as sp
left join orders as o
on o.sales_id = sp.sales_id
where o.sales_id is null 
)
select name from only_in_order
union select name from only_in_sales

-- method correct
-- When asking xxxx not have, first thinking about exclusive on this xxxx, using not in
with sales_not_in as 
(
    select o.sales_id 
    from orders as o
    left join company as cp 
    on cp.com_id = o.com_id
    where cp.name = 'RED'
)
select name
from salesperson as sp 
where sales_id not in (select * from sales_not_in)