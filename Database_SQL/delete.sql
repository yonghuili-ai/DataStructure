-- The SQL DELETE Statement
-- DELETE FROM table_name WHERE condition;
-- Example  delete from subquery
-- DELETE FROM customers WHERE customer_id IN (SELECT customer_id FROM inactive_customers);

-- Delete all rows in a table without deleting the table
-- DELETE FROM table_name;

-- Delete the table completely
-- DROP TABLE Customers;


/*
196. Delete Duplicate Emails
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
*/

-- method 1 delete from joined table
delete from person as p1 
inner join person as p2 
on p1.email = p2.email
where p1.id > p2.id
-- The above does not work, because MySQL's syntax for DELETE with a join requires a slightly different structure.

DELETE p1
FROM person p1
INNER JOIN person p2 ON p1.email = p2.email
WHERE p1.id > p2.id;
-- Explanation:
-- DELETE p1: Specifies that rows will be deleted from the alias p1.
-- FROM person p1: Defines p1 as an alias for the person table.
-- INNER JOIN person p2 ON p1.email = p2.email: Joins the table person with itself based on the email column.
-- WHERE p1.id > p2.id: The condition that determines which rows to delete. In this case, it deletes the row from p1 if there is another row in p2 with the same email but a lower id.


-- method 2 delete from tmp table
delete from person
where id not in (select min(id) from person group by email)
-- error is: You can't specify target table 'person' for update in FROM clause
-- The error "You can't specify target table 'person' for update in FROM clause" occurs in MySQL when you try to update or delete records from a table while also using that same table in a subquery within the same statement. MySQL doesn't allow direct modification of a table and its simultaneous use in a subquery due to potential conflicts and ambiguities.

-- workaround, use a CTE using min
with delete_tb as 
(
    select min(id) from person group by email
)
delete from person
where id not in (select id from delete_tb)

-- The above query will give wrong error, because column in delete_tb is named as min(id), but subquery selected id
-- to fix it, use either way in the following:
with delete_tb as 
(
    select min(id) as id from person group by email
)
delete from person
where id not in (select id from delete_tb)


with delete_tb as 
(
    select min(id) from person group by email
)
delete from person
where id not in (select * from delete_tb)



-- method 3 delete from tmp table using rank 
with delete_tb as 
(
    select id, rank() over(partition by email order by id) as rnk 
    from person
)
delete from person 
where id not in (select id from delete_tb where rnk = 1)