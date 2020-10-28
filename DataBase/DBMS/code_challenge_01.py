"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""



"""
Database handling using sqlite 
"""

import sqlite3


# File based database ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University.db' )


# creating cursor
c = conn.cursor()



# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE db_University
          (
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_no TEXT,
          Student_Branch TEXT
          )"""
          )

conn.commit()


# STEP 2
c.execute("INSERT INTO db_University VALUES ('student1', 20 , 'CSE01', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student2', 21 , 'CSE02', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student3', 20 , 'CSE03', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student4', 23 , 'CSE04', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student5', 23 , 'CSE05', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student6', 20 , 'CSE06', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student7', 21 , 'CSE07', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student8', 20 , 'CSE08', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student9', 23 , 'CSE09', 'CSE')")
c.execute("INSERT INTO db_University VALUES ('student10', 23 , 'CSE10', 'CSE')")

conn.commit()




# STEP 3
c.execute("SELECT * FROM db_University")

print ( c.fetchall() )
