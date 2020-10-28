 /*
What we want:

 OrganizationLevel = 4,
 AND 
 SalariedFlag = 1 OR JobTitle = 'Senior Tool Designer'
*/

/*
What SQL hears if we don't use parentheses:

 OrganizationLevel = 4 AND SalariedFlag = 1,
 OR 
 JobTitle = 'Senior Tool Designer'
*/

SELECT TOP (1000) [BusinessEntityID]
      ,[NationalIDNumber]
      ,[LoginID]
      ,[OrganizationNode]
      ,[OrganizationLevel]
      ,[JobTitle]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[HireDate]
      ,[SalariedFlag]
      ,[VacationHours]
      ,[SickLeaveHours]
      ,[CurrentFlag]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[HumanResources].[Employee]

  WHERE [OrganizationLevel] = 4
  AND SalariedFlag = 1
  OR JobTitle = 'Senior Tool Designer'


 /*
What SQL hears WITH parentheses:

 OrganizationLevel = 4, AND SalariedFlag = 1 OR JobTitle = 'Senior Tool Designer'
*/


SELECT TOP (1000) [BusinessEntityID]
      ,[NationalIDNumber]
      ,[LoginID]
      ,[OrganizationNode]
      ,[OrganizationLevel]
      ,[JobTitle]
      ,[BirthDate]
      ,[MaritalStatus]
      ,[Gender]
      ,[HireDate]
      ,[SalariedFlag]
      ,[VacationHours]
      ,[SickLeaveHours]
      ,[CurrentFlag]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[HumanResources].[Employee]

  WHERE [OrganizationLevel] = 4
  AND (SalariedFlag = 1
  OR JobTitle = 'Senior Tool Designer')