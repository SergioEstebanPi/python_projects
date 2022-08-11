import smtplib

to = input("Enter the email of recipient:")
content = input("Enter the content for mail:")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user='senderemail@gmail.com', password='password')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()
    
sendEmail(to, content)