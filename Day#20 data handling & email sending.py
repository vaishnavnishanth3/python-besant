#data handling using pandas:
print("PANDAS:")
print("Display Data")
import pandas as f

data={"courses":["python","java","c++"],
      "duration":[30,45,25]}
#for csv files
#data=f.read_csv("xxxxx.csv")

#raw data:
#s.no courses duration
#1    python    30
#2    java      45
#3    c++       25

df=f.DataFrame(data)
print(df)

#locate row:
print("")
print("*******************************")
print("Locate Row:")
print(df.loc[0])
print("")

#head() & tail():
#head()
print("Head():")
print("")
print(df.head(2))
print("")

#tail()
print("Tail():")
print("")
print(df.tail(2))
print("")

#remove duplicates
print("Remove Duplicates:")
print("")
print(df.drop_duplicates(inplace=True))
print("") 

#fetch a defined column
print("Fetch a column:")
print("")
print(df["duration"])
print("")

#email sending:
print("To send Email:")
for i in df["duration:"]:
    print(i)
    import smtplib
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
     # start TLS for security
    s.starttls()
     # Authentication
    s.login("Login Mail ID", "Login mail id password")
     # message to be sent
    message = "Code ran Successfully!!!"
     # sending the mail
    s.sendmail("sender mail id", i , message)
     # terminating the sessione
    s.quit()