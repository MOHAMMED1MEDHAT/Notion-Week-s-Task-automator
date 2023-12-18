import config
import time
import email_content
import app_password
import smtplib
import ssl
from email.message import EmailMessage
#Define the progress bar function
def progressBar(progress,total):
    percent=100*(progress/float(total))
    bar='█'*int(percent)+'_'*(100-int(percent))
    print(f"\r | {bar} | {percent:.2f}%",end='\r')


# Define email sender and receiver
email_sender = config.SENDER_EMAIL_ADDRESS
email_password = config.SENDER_PASSWORD
receivers_emails = list(config.RECIEVER_EMAIL_ADDRESS)

# Set the subject and body of the email
subject =email_content.subject
body =email_content.body
def send():
    progressBar(0,len(receivers_emails))
    for idx,receiver_email in enumerate(receivers_emails):
        if(idx+1)%25==0:time.sleep(5)#delay for smtp
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, app_password.gmail_app_password)
                smtp.sendmail(email_sender, receiver_email, em.as_string())
            print("done")
        except:
            print("!!ERROR!!")
        progressBar(idx+1,len(receivers_emails))
