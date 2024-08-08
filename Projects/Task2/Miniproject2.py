import requests
import os
import re
import math
from datetime import timedelta
import time
import json
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
"""
file_url = "https://github.com/logpai/loghub/blob/master/Hadoop/Hadoop_2k.log"
file_data = requests.get(file_url).content
with open("Hadoop_2k.log","wb") as file:
    file.write(file_data)

print(file_data)    

"""

k = open("E:\\Python2024\Functions\Forwhileloop\Hadoop_2k.log")
#print(k.read())
string1 = k.read()

PError = "ERROR"
error = re.findall(PError,string1)
er = len(error)
print("ERROR =",er)
#print(dir(math))
PWARN = "WARN"
warn = re.findall(PWARN,string1)
wa = len(warn)
print("WARN =",wa)
PINFO = "INFO"
info = re.findall(PINFO,string1)
inf = len(info)
print("INFO =",inf)

IP = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,4}"
v_ip = re.findall(IP,string1)
v_ip_len = len(v_ip)
print("IP Address with ports =", v_ip_len)

Sleeptime = "sleepTime=\d+"
#st = re.findall(Sleeptime,string1)
#st1 = st.group(2)
st1 = re.findall(Sleeptime,string1)
#print(st.group())
#print(st1)

Millisecond = 0
for i in range(len(st1)):
    #Millisecond = 0
    Millisecond = i * 1000

print(Millisecond)


tot = Millisecond / 1000
min = int(tot // 60)
sec = int(tot % 60)
sptime = min,sec
totalsleeptime = (str(min)+" "+"mins"+" and " + str(sec) +" "+"seconds")
#print(sec)
#print(min+"mins and"+sec)
print(totalsleeptime)


list1_input = ["Total no of Error","Total no of WARN","Total no of INFO","Total IPADDRESS","TOTALTIME"]
list2_output = [er,wa,inf,v_ip_len,totalsleeptime]
dict1 = zip(list1_input,list2_output)
#print(dict1)
set1 = (set(dict1))
dict_1=dict(set1)
print(dict_1)

with open("sample.json","w") as outfile:
    json.dump(dict_1,outfile)


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
body = f"\n Hi \n This email contains log file of \n \t {dict_1}"
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
