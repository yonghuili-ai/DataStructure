--leetcode 1454 active user
/*
Table: Accounts

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
This table contains the account id and the user name of each account.
 

Table: Logins

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| login_date    | date    |
+---------------+---------+
This table may contain duplicate rows.
This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
 

Active users are those who logged in to their accounts for five or more consecutive days.

Write a solution to find the id and the name of active users.

Return the result table ordered by id.

The result format is in the following example.

 

Example 1:

Input: 
Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+
Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+
Output: 
+----+----------+
| id | name     |
+----+----------+
| 7  | Jonathan |
+----+----------+
Explanation: 
User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.
 

Follow up: Could you write a general solution if the active users are those who logged in to their accounts for n or more consecutive days?

*/
# Write your MySQL query statement below
with dedup as
(
    select id, login_date 
    from logins
    group by 1, 2),
consecutive_5 as 
(   select id, login_date,
    lead(login_date,4) over(partition by id order by login_date) as next_4 -- use lead to find the minimum for five consecutive dates
    from dedup
)
select distinct a.id, a.name
from accounts as a
join consecutive_5 as c
on a.id = c.id
where datediff(c.next_4, login_date) = 4  -- use lead to find the minimum for five consecutive dates
order by a.id



--leetcode 180 Consecutive numbers
/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/


# Write your MySQL query statement below
with tmp as 
(select id, num, 
lead(num,1) over(order by id) as num_1, 
lead(num,2) over(order by id) as num_2,
lead(id, 1) over(order by id) as id_1,
lead(id,2) over(order by id) as id_2
from logs)
select distinct num as ConsecutiveNums
from tmp
where num = num_1 and num=num_2 and id+1 = id_1 and id+2 = id_2