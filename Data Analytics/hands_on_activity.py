
"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""





import pandas as pd

df = pd.read_csv("Salaries.csv")

# 1. Which Male and Female Professor has the highest and the lowest salaries


df1 = df[(df["salary"]==df[(df['sex']== "Female") & (df["rank"] == "Prof")]["salary"].min())]
print(df1)

# 2. Which Professor takes the highest and lowest salaries.

df1 = df[(df["salary"]==df[(df["rank"] == "Prof")]["salary"].min())]
print(df1)


df2 = df[(df["salary"]==df[(df["rank"] == "Prof")]["salary"].max())]
print(df2)





# 3. Missing Salaries - should be mean of the matching salaries of those 
#    whose service is the same

df2 =df[(df["service"] == 18)]["salary"].mean()

df1 =df[(df["service"] == 18)]

df1 = df1.fillna(df2)


print(df1)


df3 =df[(df["service"] == 2)]["salary"].mean()

df4 =df[(df["service"] == 2)]

df4 = df4.fillna(df3)

print(df4)

########## or ###########

for i in df[df["salary"].isnull()]["service"].values:
        
    df4 =df[(df["service"] == i)]
    df3 =df[(df["service"] == i)]["salary"].mean()
    df4 = df4.fillna(df3)
    print(df4)





# 4. Missing phd - should be mean of the matching service 


for i in df[df["phd"].isnull()]["service"].values:
        
    df4 =df[(df["service"] == i)]
    df3 =df[(df["service"] == i)]["phd"].mean()
    df4 = df4.fillna(df3)
    print(df4)








# 5. How many are Male Staff and how many are Female Staff. 
#    Show both in numbers and Graphically using Pie Chart.  
#    Show both numbers and in percentage


df["sex"].value_counts()


df["sex"].value_counts(normalize = True)

import matplotlib.pyplot as plt

labels = "Male","female"
sizes = [df["sex"].value_counts()[0],df["sex"].value_counts()[1]]
explode = 0,0
colors = ["yellow","pink"]
plt.pie(sizes,explode,labels,colors,  autopct='%1.2f%%', shadow=True)
plt.show()







# 6. How many are Prof, AssocProf and AsstProf. 
#    Show both in numbers adn Graphically using a Pie Chart


print(df["rank"].value_counts())

import matplotlib.pyplot as plt

labels = df["rank"].value_counts().index[0],df["rank"].value_counts().index[1],df["rank"].value_counts().index[2]

sizes = [df["rank"].value_counts().values[0],df["rank"].value_counts().values[1],df["rank"].value_counts().values[2]]

explode = 0,0,0

colors = ["R","G","B"]

plt.pie(sizes,explode,labels,colors , autopct = '%1.2f%%', shadow = True)
plt.show()







# 7. Who are the senior and junior most employees in the organization.


df["service"].sort_values().head()

df['service'].sort_values().tail()




# 8. Draw a histogram of the salaries divided into bin starting 
#    from 50K and increment of 15K





import matplotlib.pyplot as plt

a = df["salary"].sort_values().values

plt.hist(a, bins = [50000,65000,80000,95000,110000,125000,140000,155000,170000,185000,200000])

plt.axis(25000,215000)

plt.xlabel("salary")

plt.ylabel("candidate")

plt.show()










