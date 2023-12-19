import time
import fs
import smtplib
import ssl
from email.message import EmailMessage

#local imports
import config
from templates import standard

#Define the progress bar function
def progressBar(progress,total):
    percent=100*(progress/float(total))
    bar='█'*int(percent)+'_'*(100-int(percent))
    print(f"\r | {bar} | {percent:.2f}%",end='\r')


#Define app_password
app_password = config.APP_PASSWORD

# Define email sender and receiver
email_sender = config.SENDER_EMAIL_ADDRESS
receivers_emails = list(config.RECIEVERS_EMAIL_ADDRESSES)

# Set the subject and body of the email
subject =config.EMAIL_SUBJECT
if(config.EMAIL_BODY_TYPE=="html"):body = standard.body
else:body = config.EMAIL_BODY
def send():
    progressBar(0,len(receivers_emails))
    for idx,receiver_email in enumerate(receivers_emails):
        if(idx+1)%25==0:time.sleep(5)#delay for smtp
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = receiver_email
        em['Subject'] = subject

        if(config.EMAIL_BODY_TYPE=="html"):em.add_alternative(body,subtype="html")
        else:em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, app_password)
                smtp.sendmail(email_sender, receiver_email, em.as_string())
            print("done")
        except:
            print("!!ERROR!!")
        progressBar(idx+1,len(receivers_emails))
