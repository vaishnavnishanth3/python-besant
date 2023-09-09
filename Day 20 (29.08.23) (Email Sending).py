print("")
print("To send Email:")
print("")

import smtplib

login_mail_id=input("Enter your mail ID: ")
login_mail_password=input("Enter your password: ")
message = input("Enter your message to send: ")
i=input("Enter the mail id of the reciever: ") 

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(login_mail_id, login_mail_password)
s.sendmail(login_mail_id, i , message)
s.quit()

print("Email Sent Successfully")