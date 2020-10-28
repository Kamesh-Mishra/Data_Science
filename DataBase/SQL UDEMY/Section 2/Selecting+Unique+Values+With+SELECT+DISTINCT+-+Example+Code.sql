/*Selecting duplicate values from a column without SELECT DISTINCT*/

  SELECT 
       [JobTitle]

  FROM [AdventureWorks2019].[HumanResources].[Employee]


/*Selecting duplicate values from a column without SELECT DISTINCT, sorted*/

  SELECT 
       [JobTitle]

  FROM [AdventureWorks2019].[HumanResources].[Employee]

  ORDER BY 1


/*Selecting unique column values with SELECT DISTINCT*/


  SELECT DISTINCT
       [JobTitle]

  FROM [AdventureWorks2019].[HumanResources].[Employee]

  ORDER BY 1


/*Using SELECT DISTINCT across multiple columns*/


  SELECT DISTINCT
       [FirstName]
      ,[LastName]
  FROM [AdventureWorks2019].[Person].[Person]

  ORDER BY 2,1
  --ORDER BY 2,1
