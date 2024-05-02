-- leetcode 1045. Customers Who Bought All Products
/*Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows. 
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.
 

Table: Product

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.
 

Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The result format is in the following example.*/
with tmp as 
(select distinct customer_id, product_key from customer)
select customer_id
from tmp 
group by 1
having count(distinct product_key) = 
(select count(product_key) from product)
-- also works and faster
with tmp as 
(select distinct customer_id, product_key from customer)
select customer_id
from tmp 
right join product as p 
on tmp.product_key = p.product_key
group by 1
having count(tmp.product_key) = (select count(1) from product) 