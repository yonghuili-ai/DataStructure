-- leetcode 184 highest salary
# Write your MySQL query statement below
/*when you group by department ID,you can only get aggregates of columns like min,max etc.,you can't get which row that max or min corresponds to..think of it as a summary of a group..you don't get row level insights after group by..

need to ask if there are multiple highest salary in the same department, then we can not use group by department id which will return wrong employee name

for example, this question in Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.*/

with tmp as (
select d.name as Department, e.name as Employee, e.salary,
dense_rank() over(partition by d.name order by e.salary desc) as rnk
from employee as e
join department as d 
on e.departmentid = d.id 
)
select Department, Employee, salary
from tmp
where rnk = 1


-- leetcode 176 Second highest salary ==> how to return null if not found?
# Write your MySQL query statement below
/*However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table. To overcome this issue, we can take this as a temp table. */

/*must contain distinct otherwise duplicated cases will return a value, but not null -- as required*/
select 
(select distinct salary 
from employee
order by salary desc 
limit 1
offset 1) as SecondHighestSalary