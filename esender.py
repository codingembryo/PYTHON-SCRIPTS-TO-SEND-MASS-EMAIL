#import the necessary module
import smtplib, ssl, csv
from email.message import EmailMessage



sender = ''
password = ''#type the app password you geenrated

subject = 'Looking for a remote job?'#add the subject
body_message = 'Check out this page'#Type the message


#connect to outgoing mail sender
context = ssl.create_default_context()
server =  smtplib.SMTP_SSL('smtp.gmail.com', 587, context = context)
server.login(sender, password)

#Formula to send email
with open('C:\\Users\\23470\\Desktop\\newme.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        server.send_message(em)
        print("message sent")


server.close()
print('done')





