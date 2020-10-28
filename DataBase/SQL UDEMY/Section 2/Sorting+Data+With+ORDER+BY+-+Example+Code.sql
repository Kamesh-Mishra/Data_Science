/*ORDER BY DESC*/
SELECT [SalesOrderID]
      ,[OrderDate]
      ,[TotalDue]

  FROM [AdventureWorks2019].[Sales].[SalesOrderHeader]

  WHERE [TotalDue] > 10000

  ORDER BY [TotalDue] DESC


  /*ORDER BY ASC*/
SELECT [SalesOrderID]
      ,[OrderDate]
      ,[TotalDue]

  FROM [AdventureWorks2019].[Sales].[SalesOrderHeader]

  WHERE [TotalDue] > 10000

  ORDER BY [TotalDue] ASC --Alternately, just use ORDER BY [TotalDue] here


/*ORDER BY referencing column alias*/
SELECT [SalesOrderID]
      ,[OrderDate]
      ,[Total Amount Due] = [TotalDue]

  FROM [AdventureWorks2019].[Sales].[SalesOrderHeader]

  WHERE [TotalDue] > 10000

  ORDER BY [Total Amount Due] DESC


/*ORDER BY referencing column position*/
SELECT [SalesOrderID]
      ,[OrderDate]
      ,[Total Amount Due] = [TotalDue]

  FROM [AdventureWorks2019].[Sales].[SalesOrderHeader]

  WHERE [TotalDue] > 10000

  ORDER BY 3 DESC



/*ORDER BY First Name ONLY*/

SELECT [BusinessEntityID]
      ,[PersonType]
      ,[NameStyle]
      ,[Title]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[Suffix]
      ,[EmailPromotion]
      ,[AdditionalContactInfo]
      ,[Demographics]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[Person].[Person]

  ORDER BY [FirstName]



/*ORDER BY First Name and Last Name*/

SELECT [BusinessEntityID]
      ,[PersonType]
      ,[NameStyle]
      ,[Title]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[Suffix]
      ,[EmailPromotion]
      ,[AdditionalContactInfo]
      ,[Demographics]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[Person].[Person]

  ORDER BY [FirstName], [LastName]