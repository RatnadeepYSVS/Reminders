from smtplib import *
from datetime import *
username=input('Please Enter Your Name ')
obj=SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
email=input('Enter Your Email ')
passcode=input('Enter Your Passcode:-')#must be your app passcode not your gmail passcode.Kindly google it or check in youtube if not known.
obj.login(email,passcode)
z=list()
while True:
    try:
        s,k=map(str,input('Please Add The Reminder And Time.').split())
        z=z+[[k,s]]
    except:
        break
z.sort()
for i in enumerate(list(z)):
    while True:
        if datetime.now().hour==int(i[1][0].split(':')[0]) and datetime.now().minute==int(i[1][0].split(':')[-1]):
            subject=f'Reminder:-{int(i[0])+1}'
            mess=f'Hello {username}\n.You have a reminder\n.Reminder:-{i[1][1]}'
            msg=f'Subject: {subject}\n\n{mess}'
            obj.sendmail(email,email,msg)
            break
