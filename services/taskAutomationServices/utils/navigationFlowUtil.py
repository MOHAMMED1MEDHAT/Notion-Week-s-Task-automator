from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys

#local imports
import xPathLocationsUtil as xpLocations

def addTask(driver,taskDate,task):
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
    setDate_dialog.set_attribute("text",taskDate)
    #9 click done btn
    done_btn=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.done_btn_XP))
    done_btn.click()
    #10 click chooseType dropdownBtn
    chooseType_dropdownBtn=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.chooseType_dropdownBtn_XP))
    chooseType_dropdownBtn.click()
    #11 click typeOption
    typeOption=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.typeOption_XP.format(taskType=task["type"])))
    typeOption.click()
    #12 click save btn
    save_btn=WebDriverWait(driver,timeout=50).until(lambda el:el.find_element(By.XPATH,xpLocations.save_btn_XP))
    save_btn.click()
    #13 click create task btn
    createTasks_btn = WebDriverWait(driver, timeout=50).until(lambda el: el.find_element(By.XPATH,xpLocations.createTasks_btn_XP))
    createTasks_btn.click()