--Exercise 1:
--Select all columns AND rows from the “Sales.Customer” table.

SELECT
*
FROM [AdventureWorks2019].[Sales].[Customer]



--Exercise 2:
--Select all columns and the top 100 rows from the “Production.Product” table.

SELECT TOP (1000) 
*
FROM [AdventureWorks2019].[Production].[Product]