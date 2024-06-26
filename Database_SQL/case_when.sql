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

--leetcode 1393. Capital Gain/Loss

/*Table: Stocks

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
The operation column is an ENUM (category) of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day. It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.
 

Write a solution to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Stocks table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+
Output: 
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+
Explanation: 
Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$ and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$. Capital gain/loss is the sum of capital gains/losses for each ('Buy' --> 'Sell') operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.*/

-- use case when inside sum
select stock_name,
sum(case when operation = 'Buy' then -1 * price when operation = 'Sell' then price end ) as capital_gain_loss
from stocks
group by 1




!! 1783


-- leetcode 1699. Number of Calls Between Two Persons !!!
/*
Table: Calls

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
This table does not have a primary key (column with unique values), it may contain duplicates.
This table contains the duration of a phone call between from_id and to_id.
from_id != to_id
 

Write a solution to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Calls table:
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
Output: 
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+
Explanation: 
Users 1 and 2 had 2 calls and the total duration is 70 (59 + 11).
Users 1 and 3 had 1 call and the total duration is 20.
Users 3 and 4 had 4 calls and the total duration is 999 (100 + 200 + 200 + 499).
*/
-- Solution 1
with tmp 
as
(select from_id as person1, to_id as person2, duration 
from Calls
where from_id < to_id
union all 
select to_id as person1, from_id as person2, duration 
from Calls
where to_id < from_id)
select person1, person2, count(*) as call_count, sum(duration) as total_duration
from tmp 
group by 1, 2


-- The other solution
select 
case when from_id < to_id then from_id else to_id end as person1,
case when from_id < to_id then to_id else from_id end as person2,
count(*) as call_count,
sum(duration) as total_duration
from calls
group by 1, 2



/*
Leetcode 1179 https://leetcode.com/problems/reformat-department-table/description/

we could get a revenue for each month by using aggregate function such as SUM, MAX or MIN because these functions ignore the null values.

As the table description, the group of (id, month) is the primary key. Hence, we know there could not be more than two valid revenue values for each month of each id

pivot or flat or reform a table, use this sum/max/min(case when   ) as structure
*/

-- can be simplified as the next query
with monthly_tb as 
(
    select id, 
    case when month = 'Jan' then revenue else null end as Jan_Revenue, 
    case when month = 'Feb' then revenue else null end as Feb_Revenue, 
    case when month = 'Mar' then revenue else null end as Mar_Revenue, 
    case when month = 'Apr' then revenue else null end as Apr_Revenue, 
    case when month = 'May' then revenue else null end as May_Revenue, 
    case when month = 'Jun' then revenue else null end as Jun_Revenue, 
    case when month = 'Jul' then revenue else null end as Jul_Revenue, 
    case when month = 'Aug' then revenue else null end as Aug_Revenue, 
    case when month = 'Sep' then revenue else null end as Sep_Revenue, 
    case when month = 'Oct' then revenue else null end as Oct_Revenue, 
    case when month = 'Nov' then revenue else null end as Nov_Revenue, 
    case when month = 'Dec' then revenue else null end as Dec_Revenue
    from department)
select id, 
max(Jan_Revenue) as Jan_Revenue,
max(Feb_Revenue) as Feb_Revenue,
max(Mar_Revenue) as Mar_Revenue,
max(Apr_Revenue) as Apr_Revenue,
max(May_Revenue) as May_Revenue, 
max(Jun_Revenue) as Jun_Revenue,
max(Jul_Revenue) as Jul_Revenue, 
max(Aug_Revenue) as Aug_Revenue,
max(Sep_Revenue) as Sep_Revenue,
max(Oct_Revenue) as Oct_Revenue, 
max(Nov_Revenue) as Nov_Revenue, 
max(Dec_Revenue) as Dec_Revenue
from monthly_tb
group by id 

-- simplified version
select id, 
max(case when month = 'Jan' then revenue end) as Jan_Revenue, 
max(case when month = 'Feb' then revenue end)as Feb_Revenue, 
max(case when month = 'Mar' then revenue end) as Mar_Revenue, 
max(case when month = 'Apr' then revenue end) as Apr_Revenue, 
max(case when month = 'May' then revenue end) as May_Revenue, 
max(case when month = 'Jun' then revenue end)as Jun_Revenue, 
max(case when month = 'Jul' then revenue end) as Jul_Revenue, 
max(case when month = 'Aug' then revenue end) as Aug_Revenue, 
max(case when month = 'Sep' then revenue end) as Sep_Revenue, 
max(case when month = 'Oct' then revenue end) as Oct_Revenue, 
max(case when month = 'Nov' then revenue end) as Nov_Revenue, 
max(case when month = 'Dec' then revenue end) as Dec_Revenue
from Department
group by id 




