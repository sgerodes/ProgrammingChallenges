SELECT Name AS Employee
FROM (
    SELECT e1.*
    FROM Employee e1, Employee e2
    WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
    ) AS goldnuggets;