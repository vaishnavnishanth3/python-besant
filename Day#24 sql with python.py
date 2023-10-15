print("")
#install and import mysql connector
print("Sql:")
import mysql.connector
#connect sql with python
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="new_db"
)
print(mydb)
print("")
#python-------->mysql
#python<--------python

mycursor=mydb.cursor()
#insert data into db

print("Insert a data:")
sql="insert into python_students (firstname,lastname,fees,adress) values (%s,%s,%s,%s)"

firstname=input("Enter your firstname: ")
lastname=input("Enter your lastname: ")
fees=input("Enter your fee detail: ")
adress=input("Enter your adress: ")

val=(firstname,lastname,fees,adress)

mycursor.execute(sql,val)
mydb.commit() #to save data
print("Data Saved Successfully!!!")
print("")

print("View all Data:")
mycursor.execute("select * from python_students")
myresult=mycursor.fetchall()

start=int(input("Enter Start Row: "))
end=int(input("Enter End Row: "))
for i in myresult:
    print(i)
    print(i[start:end+1])
print("")

print("Update a data:")
sql="update python_students set fees='Not Paid' where firstname='Vaishnav'"
mycursor.execute(sql)
mydb.commit()
print("Updated successfully")
print("")

print("Delete a data:")
#if input is required:
columnname=input("Enter the Column you want to delete: ")
delete_col=input("Enter the specific data to be delete from the column: ")
sql=f"delete from python_students where {columnname}='{delete_col}'"
mycursor.execute(sql)
mydb.commit()
print("Deleted Successfully")
print("")