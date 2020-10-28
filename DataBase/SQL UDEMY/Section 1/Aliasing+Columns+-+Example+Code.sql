--Aliasing a column name in SQL
SELECT 
       [Organization Level] = [OrganizationLevel]
      ,[Job Title] = [JobTitle]
      ,[Hire Date] = [HireDate]
      ,[Vacation Hours] = [VacationHours]
	  
FROM [AdventureWorks2019].[HumanResources].[Employee]