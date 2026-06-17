# Write your MySQL query statement below




SELECT  
    d.name as Department,
    e1.name as Employee,
    e1.salary as Salary
FROM Employee e1
INNER JOIN Department d  ON  e1.departmentId = d.id
WHERE 3 > (
    select count(distinct (e2.Salary))
            from  Employee e2
            where e2.Salary > e1.Salary
            and e1.DepartmentId = e2.DepartmentId
    
);
    