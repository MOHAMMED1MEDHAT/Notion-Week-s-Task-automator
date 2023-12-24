from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys

#local imports
import xPathLocationsUtil as xpLocations

def addTask(driver,task):
    #1 hover over the create tasks btn
    createTasks_btn = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.createTasks_btn_XP))
    hover = ActionChains(driver)
    hover.move_to_element(createTasks_btn).perform()
    #2 click settings btn
    settings_btn = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.settings_btn_XP))
    settings_btn.click()
    #3 click the name txtbx.set_attribute("{taskName}")
    name_txtbx = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.name_txtbx_XP))
    name_txtbx.send_keys(str(task["name"]))
    #4 click the status dropdownBtn
    status_dropdownBtn = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.status_dropdownBtn_XP))
    status_dropdownBtn.click()
    #5 click the task option
    if(task["status"]=="not started"):
        not_started_option = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.not_started_option_XP))
        not_started_option.click()
    elif(task["status"]=="in progress"):
        in_progress_option = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.in_progress_option_XP))
        in_progress_option.click()
    #6 click chooseDate dropdownBtn
    chooseDate_dropdownBtn=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.chooseDate_dropdownBtn_XP))
    chooseDate_dropdownBtn.click()
    #7 click pickDate btn
    pickDate_btn=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.pickDate_btn_XP))
    pickDate_btn.click()
    #8 enter date dialog set_attribute("text","Dec 20,2023")
    setDate_dialog=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.setDate_dialog_XP))
    #9 click done btn
    #10 click chooseType dropdownBtn
    #11 click typeOption
    #12 click save btn
    #Dashboard--------------------------------------------------------
    dashboard_a = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,assests.DASHBOARD))
    dashboard_a.click()

    #access the event-----------------------------------------------------------
    event_frame = WebDriverWait(driver, timeout=110).until(lambda el: el.find_element(By.XPATH,assests.EVENT))
    event_frame.click()

    #edit the event--------------------------------------------------------------
    add_attendee_btn= WebDriverWait(driver, timeout=130).until(lambda el: el.find_element(By.XPATH,assests.ADD_ATTENDEE))
    add_attendee_btn.click()

    #add the attendees----------------------------------------------------------
    def addAttendee(attendees):
        assests.progressBar(0,len(attendees))
        for idx,attendee in enumerate(attendees):
            #insert the attendee first name
            first_name=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.FIRSTNM))
            first_name.send_keys(str(attendee["firstName"]))

            #insert the attendee last name
            last_name=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.LASTNM))
            last_name.send_keys(str(attendee["lastName"]))

            #insert the attendee mail
            email=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.EMAIL))
            email.send_keys(str(attendee["email"]))

            #check if check in is marked
            if(assests.CHECKIN_FLAG):
                check_in=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.CHECKIN))
                if(idx==0):
                    check_in.click()
                else:
                    check_in.click()
                    check_in.click()

            #check if send event mail is marked
            if(not(assests.SENDEMAL_FLAG)):
                send_email=WebDriverWait(driver,timeout=150).until(lambda el:el.find_element(By.XPATH,assests.SENDMAIL))
                send_email.click()


            #check if it finished or not
            if(idx==len(attendees)-1):
                done=WebDriverWait(driver,timeout=160).until(lambda el:el.find_element(By.XPATH,assests.ADD))
                done.click()
            else:
                more=WebDriverWait(driver,timeout=160).until(lambda el:el.find_element(By.XPATH,assests.SAVE_AND_CONT))
                more.click()
            time.sleep(2)
            assests.progressBar(idx+1,len(attendees))

    # addAttendee(attendees)

