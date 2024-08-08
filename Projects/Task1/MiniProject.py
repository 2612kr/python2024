"""Task/project: 

1. Get resume from user (as text file or word) (you can use your resume)
2. Check whether file is empty or not 
3. Extract below details from resume mobile number, email address, GitHub/LinkedIn id, all numbers in resume, date of birth
4. Using extracted date of birth, calculate age of the person 
5. Send extracted details as mail to your mail id (study SMTP and email module). https://realpython.com/python-send-email/
"""

import os
import re
from datetime import datetime
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

z = open("E:\\Python2024\\Functions\\Forwhileloop\\resume.txt")
string = z.read()
#print(dir(os))

z.seek(0) #Unecessary but important if file was manipulated before reading
if z.read() == '':
    print("no data found")
else:
    print("Data present in file")


ext_mob = "\d{10}"
val_mob = re.findall(ext_mob,string)
print("Mobile",val_mob)
ext_dob = "(\d{2})-(\d{2})-(\d{4})" #'(\d{2})-(\d{2})-(\d{4})'
dob = re.findall(ext_dob,string)
print("DOB",dob)
ext_email ='\S+@\S+'
val_email = re.findall(ext_email,string)
print("Email",val_email)
ext_linkind = "(?P<url>https?://[^\s]+)"
val_linkind = re.findall(ext_linkind,string)
print("LinkedIn",val_linkind)

dob1 = "17-05-1999"
birth = datetime.strptime(dob1,"%d-%m-%Y")
today = datetime.today()
age = today.year - birth.year # (today.month, today.day) # (dob.month, dob.day))
    

print((age))


"""import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("krtech26@gmail.com", "sender_email_id_password")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("krtech26@gmail.com", "krtech26@outlook.com", message)
# terminating the session
s.quit()"""


# Set up the SMTP server connection
smtp_server = 'outlook.office365.com'
smtp_port = 587  # Use 465 for SSL or 587 for TLS

sender_email = 'krtech26@outlook.com'
receiver_email = 'krtech26@gmail.com'
password = 'Opendoors@11'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Test mail from Kamal'

# Add body to email
body = f"\n Hi \n This email contains Candiate details \n \t MobileNumber:{val_mob},\n\t Date of Birth:{dob},\n\t Email Address:{val_email},\n\t LinkedIn:{val_linkind}"
msg.attach(MIMEText(body, 'plain'))

# Send the message via SMTP server.
try:
    server_ssl = smtplib.SMTP(smtp_server, smtp_port)
    server_ssl.starttls()
    server_ssl.login(sender_email, password)
    server_ssl.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print(f'Error: {e}')

server_ssl.quit()
