
"""

Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""



import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:FZMv8d5qWCSjb8z@cluster0-4fycb.mongodb.net/db_University?retryWrites=true&w=majority")
mydb = client.db_University


def add_db_University(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    unique_db_University = mydb.db_University_coll.find_one({"Student_Name":Student_Name})
    if unique_db_University:
        return " already exists"
    else:
        mydb.db_University_coll.insert_one(
                {
                "Studnet_Name" : Student_Name,
                "Student_Age" : Student_Age,
                "Student_Roll_no" : Student_Roll_no,
                "Student_Branch" : Student_Branch
                })
        return "db_University added successfully"


def fetch_all_db_University():
    user = mydb.db_University_coll.find()
    for i in user:
        print (i)




#Insert data in collection

add_db_University('student1', 20 , 'CSE01', 'CSE')
add_db_University('student2', 21 , 'CSE02', 'CSE')
add_db_University('student3', 20 , 'CSE03', 'CSE')
add_db_University('student4', 23 , 'CSE04', 'CSE')
add_db_University('student5', 23 , 'CSE05', 'CSE')
add_db_University('student6', 20 , 'CSE06', 'CSE')
add_db_University('student7', 21 , 'CSE07', 'CSE')
add_db_University('student8', 20 , 'CSE08', 'CSE')
add_db_University('student9', 23 , 'CSE09', 'CSE')
add_db_University('student10', 23 , 'CSE10', 'CSE')

fetch_all_db_University()



