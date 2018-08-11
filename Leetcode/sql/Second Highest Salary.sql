SELECT IFNULL(
               (SELECT DISTINCT Salary
                FROM employee
                ORDER BY Salary DESC
                LIMIT 1 OFFSET 1
                )
                ,NULL) AS SecondHighestSalary
;