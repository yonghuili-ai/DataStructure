/*UPDATE Syntax
1) UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

Example:
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
WHERE CustomerID = 1;

Why does not need to include from in update?

Because:
In MySQL, the UPDATE syntax does not include the FROM clause directly as seen in some other SQL databases like SQL Server or PostgreSQL. Instead, MySQL uses a different syntax for performing updates that involve joins or subqueries. The MySQL UPDATE statement is designed to be straightforward, where you specify the table to update, the columns to set, and the conditions for the update.

2) Updates with Joins
UPDATE table1 as t1
JOIN table2 as t2 on t1.id = t2.com_id
SET t1.column1 = value1, t1.column2 = value2
WHERE condition

UPDATE employees e
JOIN departments d ON e.department_id = d.department_id
SET e.salary = e.salary * 1.10
WHERE d.department_name = 'Sales';

3) Update with subquery

UPDATE employees
SET salary = salary * 1.10
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = 'Sales');


*/

-- 627 https://leetcode.com/problems/swap-salary/
/*
Table: Salary

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM (category) value of type ('m', 'f').
The table contains information about an employee.
 

Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

The result format is in the following example.

 

Example 1:

Input: 
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
Output: 
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
Explanation: 
(1, A) and (3, C) were changed from 'm' to 'f'.
(2, B) and (4, D) were changed from 'f' to 'm'.
*/

-- wrong, should not use from
update salary
set sex=(case sex when 'f' then 'm' when 'm' then 'f' end from salary)


-- correct
update salary
set sex=(case sex when 'f' then 'm' when 'm' then 'f' end)