-- leetcode 626. Exchange Seats
/*
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.
*/
select 
(case when id%2 and id=(select count(*) from seat) then id
when id%2 then id + 1
when not id%2 then id - 1 end --else id-1
) as id,
student from seat
order by id



--leetcode 1777 product's price for each store

/*
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | enum    |
| price       | int     |
+-------------+---------+
In SQL, (product_id, store) is the primary key for this table.
store is a category of type ('store1', 'store2', 'store3') where each represents the store this product is available at.
price is the price of the product at this store.
 

Find the price of each product in each store.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
Output: 
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+
Explanation: 
Product 0 price's are 95 for store1, 100 for store2 and, 105 for store3.
Product 1 price's are 70 for store1, 80 for store3 and, it's not sold in store2.
*/

/*Using MAX, CASE WHEN to pivot
Intuition
We will pivot our table by utilizing CASE WHEN and AS to produce new rows in our resulting table. While pivoting using CASE WHEN, it will not automatically group rows of the same product_id to fill the next available value, thus resulting in a null price and a singular product_id.

To resolve this, we can use aggregation functions MAX, MIN, or SUM on the column price to grab the next available price for each product_id rather than returning null and using GROUP BY to separate by unique product_ids. The role of the MAX function here is to ensure that only one row of results is returned for each product and to select the correct price for each store.*/

select product_id, 
max(case when store='store1' then price end) as store1,
max(case when store='store2' then price end) as store2,
max(case when store='store3' then price end) as store3
from products
group by 1