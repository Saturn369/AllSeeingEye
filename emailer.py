import smtplib
import config
import datetime
import txtParser

global subject, msg


def initialize():
    global subject, msg
    
    oldHour = datetime.datetime.now().hour #Store the hour portion of the date in a variable for comparison and manipulation later on

    subject = "Testing" #Subject text of the email to be sent

    msg = txtParser.file_read(r"C:\Users\DrapelickClient2\Desktop\pyproject\Emailsss\log.txt") #Inner message component of the email




def send_email(subject, msg):#Using the built in server library, I create the function to send an email here
    try:
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.PASSWORD, config.EMAIL_ADDRESS, message)
        server.quit()
        print('Email sent successfully')
    except:
        print('Try again')


def main():


    
    initialize()
    
    send_email(subject, msg)
    
    '''while True:#This algorithm with run in perpetuity or until stopped. Its purpose is to run the send_email function every x hours
        if oldHour == 23 and datetime.datetime.now().hour == 0:
            oldHour = -1
        
        if oldHour - datetime.datetime.now().hour < -1:
            oldHour = datetime.datetime.now().hour
            send_email(subject, msg)'''

