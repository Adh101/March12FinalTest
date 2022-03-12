SELECT dept.Name AS Department,emp1.Name AS Employee, emp1.Salary AS Salary FROM Employee AS emp1 INNER JOIN Department dept
ON emp1.DepartmentID = dept.Id
WHERE 3 > (
           SELECT COUNT(DISTINCT Salary)
           FROM Employee AS emp2
           WHERE emp2.Salary > emp1.Salary
           AND emp1.DepartmentID = emp2.DepartmentID
          )
ORDER BY Department ASC, Salary DESC;
