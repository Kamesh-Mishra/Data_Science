"""
Code Challenge
  Name: 
    Exploratory Data Analysis - Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people survived the disaster ?
      How many people died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""


import pandas as pd
#Read csv file
df = pd.read_csv("training_titanic.csv")

# Not a good technique to print the Data Frame
#print (df)

#df["Survived"]

print("people survived the disaster :",df["Survived"].value_counts()[1])

print("people Died :",df["Survived"].value_counts()[0])



print("Survival rates %  :",df["Survived"].value_counts(normalize = True)[1]*100,"%")

#or

#print("Survival rates %  :",df["Survived"].value_counts(1)[1]*100,"%")


df.groupby(["Survived","Sex"])


df_sub= df[(df['Survived'] == 1) & \
           (df['Sex'] == "male")]



print("males Survived :",df_sub.count()["Survived"])


df_sub2= df[(df['Survived'] == 0) & \
           (df['Sex'] == "male")]

    
print("males passed away : ",df_sub2.count()["Survived"])



df_sub= df[(df['Survived'] == 1) & \
           (df['Sex'] == "female")]



print("females Survived :",df_sub.count()["Survived"])


df_sub2= df[(df['Survived'] == 0) & \
           (df['Sex'] == "female")]

    
print("females passed away : ",df_sub2.count()["Survived"])





df["categorical"] = df["Age"].map(lambda x: 1 if x < 18 else 0 )

#print("Age categorical column : \n",df["categorical"])

print("chlid less then 18 age :",(df["categorical"]==1).value_counts()[1])

print("people greater then 18 age :",(df["categorical"]==1).value_counts()[0])


df_sub3 = df[(df['Survived'] == 1) & \
           (df['categorical'] == 1)]

print("child survived less then 18 age :",df_sub3.count()[1])
print("child survived %, less then 18 age :",(df_sub3.count()[1]/df["Survived"].value_counts()[1])*100,"%")


df_sub4 = df[(df['Survived'] == 1) & \
           (df['categorical'] == 0)]




print("people survived greater then 18 age :",df_sub4.count()[1])

print("people survived greater then 18 age :",(df_sub4.count()[1]/df["Survived"].value_counts()[1])*100,"%")







