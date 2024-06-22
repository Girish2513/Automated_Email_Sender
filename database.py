import pymysql
import schedule
import time
from datetime import date
from emailsender import send_email
myobj=pymysql.connect(host='localhost',user='root',password='',db='feedetails')
cursor=myobj.cursor()
a=cursor.execute('select * from `students`')
output = cursor.fetchall() 
today=date.today()
emailsent=0
for i in output:
    if i[7]<today:
        send_email('Fee Remainder',i[3],i[1],i[7],i[6],i[5],i[2])
        emailsent+=1
        time.sleep(2)
print(emailsent)
