import pandas as pd
"""
Series and DataFrame

I may be kind of obvious talking about Series and DataFrame for someone who is already accustomed to using Panda, but I want to make it clear for those who are getting started, about the main difference between these two types of data structure.

    Series is nothing more than an array of 1 dimension. You can also consider a Series as a column of a table. Example:
"""
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

"""  A DataFrame is simply a set of Series. It is a 2-dimensional data structure — columns and rows — that transforms the data into a beautiful table. Example:
"""
#Creating a dictionary where each key will be a DataFrame column
        
data = {'País': ['Bélgica', 'Índia', 'Brasil'],
                                'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
                                'População': [123465, 456789, 987654]}
    
#Creating the DataFrame
    
df = pd.DataFrame(data, columns=['País','Capital','População'])


#Opening and writing CSV files

#Reading a CSV files
pd.read_csv('file_name.csv')#Reading a CSV files encoded in ISO-8859-1
pd.read_csv('file_name.csv', encoding = 'ISO-8859-1')#Writing a CSV files
pd.to_csv("name_of_the_file_to_save.csv")
          
          
          #Opening Excel Files

xlsx = pd.ExcelFile('your_excel_file.xlsx')
df = pd.read_excel(xlsx, 'Sheet 1')

#Removing rows and columns

#Removing rows by index
s.drop([0, 1])#Remove columns using the argument 'axis = 1'
df.drop('Country', axis = 1)


#Collecting basic information about the DataFrame

#Amount of Rows and Columns
df.shape#Index Description
df.index#Columns in the DataFrame
df.columns#Non-null data counts
df.count()



#Creating a new column in a DataFrame

#It'll create a column called 'New Column' with 0 as its value
df['New Column'] = 0



#Renaming columns from a DataFrame

#If your DataFrame has 3 columns, pass 3 new values in a list
df.columns = ['Column 1', 'Column 2', 'Column 3']






#Summary of data

#Sum of values in a DataFrame
df.sum()#Lowest value of a DataFrame
df.min()#Highest value
df.max()#Index of the lowest value
df.idxmin()#Index of the highest value
df.idxmax()#Statistical summary of the DataFrame, with quartiles, median, etc.
df.describe()#Average values
df.mean()#Median values
df.median()




#Applying functions

#Applying a function that replaces 'a' by 'b'
df.apply(lambda x: x.replace('a', 'b'))






#Ordering values

#Ordering in ascending order
df.sort_values()#Ordering in descending order
df.sort_values(ascending = False)



#Arithmetic operations in Series

#Example
s = pd.Series ([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])#Suming all values in the Series by 2
s.add(2)#Subtracting 2 of all values
s.sub(2)#Multiplying values by 2
s.mul(2)#Dividing values by 2
s.div(2)



#Boolean Indexing

#Filtering DataFrame to show only even values
df[df['Population']% 2 == 0]



#Selecting values

#Selecting the first row of the Country column
df.loc([0],['Country'])








