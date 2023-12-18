from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys

#local imports
import assests


# # from readAttendees import attendees

# def args_manger(args):
#     if(len(args)==2):assests.SESSIONID=args[1]
#     elif(len(args)==3):
#         assests.SESSIONID=args[1]
#         if(args[2]=='t' or args[2]=='T'):assests.CHECKIN_FLAG=True
#         else:assests.CHECKIN_FLAG=False
#     elif(len(args)==4):
#         assests.SESSIONID=args[1]
#         if(args[2]=='t' or args[2]=='T'):assests.CHECKIN_FLAG=True
#         else:assests.CHECKIN_FLAG=False
#         if(args[3]=='t' or args[3]=='T'):assests.SENDEMAL_FLAG=True
#         else:assests.SENDEMAL_FLAG=False
# args_manger(sys.argv)

# #Change chrome driver path accordingly
# # PATH= r"C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome()
# driver.get("https://gdsc.community.dev/mansoura-university/")
# driver.add_cookie({"name":"sessionid","value":assests.SESSIONID})
# driver.refresh();

# #Dashboard--------------------------------------------------------
# dashboard_a = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,assests.DASHBOARD))
# dashboard_a.click()

# #access the event-----------------------------------------------------------
# event_frame = WebDriverWait(driver, timeout=110).until(lambda el: el.find_element(By.XPATH,assests.EVENT))
# event_frame.click()

# #edit the event--------------------------------------------------------------
# add_attendee_btn= WebDriverWait(driver, timeout=130).until(lambda el: el.find_element(By.XPATH,assests.ADD_ATTENDEE))
# add_attendee_btn.click()

# #add the attendees----------------------------------------------------------
# def addAttendee(attendees):
#     assests.progressBar(0,len(attendees))
#     for idx,attendee in enumerate(attendees):
#         #insert the attendee first name
#         first_name=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.FIRSTNM))
#         first_name.send_keys(str(attendee["firstName"]))

#         #insert the attendee last name
#         last_name=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.LASTNM))
#         last_name.send_keys(str(attendee["lastName"]))

#         #insert the attendee mail
#         email=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.EMAIL))
#         email.send_keys(str(attendee["email"]))

#         #check if check in is marked
#         if(assests.CHECKIN_FLAG):
#             check_in=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.CHECKIN))
#             if(idx==0):
#                 check_in.click()
#             else:
#                 check_in.click()
#                 check_in.click()

#         #check if send event mail is marked
#         if(not(assests.SENDEMAL_FLAG)):
#             send_email=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.SENDMAIL))
#             send_email.click()


#         #check if it finished or not
#         if(idx==len(attendees)-1):
#             done=WebDriverWait(driver,timeout=160).until(lambda el:el.find_element(By.XPATH,assests.ADD))
#             done.click()
#         else:
#             more=WebDriverWait(driver,timeout=160).until(lambda el:el.find_element(By.XPATH,assests.SAVE_AND_CONT))
#             more.click()
#         time.sleep(2)
#         assests.progressBar(idx+1,len(attendees))

# # addAttendee(attendees)

# driver.quit()