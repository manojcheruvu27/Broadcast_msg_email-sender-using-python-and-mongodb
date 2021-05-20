import details as dt
import smtplib
import email.utils

sender_email = "place your email id over here"
password  = "type your password"
message = "Tommorow is a holiday!!!"
#Server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("Login success")

for i in dt.getemail():
    server.sendmail(sender_email,i,message)
    print("Email has been sent to",i)
