/*Inequality example*/

SELECT [BusinessEntityID]
      ,[TerritoryID]
      ,[SalesQuota]
      ,[Bonus]
      ,[CommissionPct]
      ,[SalesYTD]
      ,[SalesLastYear]
      ,[rowguid]
      ,[ModifiedDate]
	  
FROM [AdventureWorks2019].[Sales].[SalesPerson]

WHERE [SalesQuota] != 250000



/*Using IS NULL*/

SELECT [BusinessEntityID]
      ,[TerritoryID]
      ,[SalesQuota]
      ,[Bonus]
      ,[CommissionPct]
      ,[SalesYTD]
      ,[SalesLastYear]
      ,[rowguid]
      ,[ModifiedDate]
	  
FROM [AdventureWorks2019].[Sales].[SalesPerson]

WHERE [SalesQuota] IS NULL


/*Using IS NOT NULL*/

SELECT [BusinessEntityID]
      ,[TerritoryID]
      ,[SalesQuota]
      ,[Bonus]
      ,[CommissionPct]
      ,[SalesYTD]
      ,[SalesLastYear]
      ,[rowguid]
      ,[ModifiedDate]
	  
FROM [AdventureWorks2019].[Sales].[SalesPerson]

WHERE [SalesQuota] IS NOT NULL




/*Combining inequalities and NULLs*/

SELECT [BusinessEntityID]
      ,[TerritoryID]
      ,[SalesQuota]
      ,[Bonus]
      ,[CommissionPct]
      ,[SalesYTD]
      ,[SalesLastYear]
      ,[rowguid]
      ,[ModifiedDate]
	  
FROM [AdventureWorks2019].[Sales].[SalesPerson]

WHERE [SalesQuota] != 250000 OR [SalesQuota] IS NULL
