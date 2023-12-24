from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import subprocess

#local imports
import config
from services.taskAutomationServices.utils.navigationFlowUtil   import addTask
from services.taskAutomationServices.utils import xPathLocationsUtil as xpLocations

def startService():
    #1-open chrome in debuging mode
    # subprocess.run("taskkill /F /IM \"chrome.exe\"", shell=True)
    # subprocess.run(f"chrome --remote-debugging-port={str(config.CHROME_DEBUGING_PORT)}", shell=True)
    subprocess.run("chrome --remote-debugging-port=9222", shell=True)

    #2- connect to chrome
    # chromeDebuggingServerLink=f"127.0.0.1:{str(config.CHROME_DEBUGING_PORT)}"

    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", chromeDebuggingServerLink)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.get(config.NOTION_TASK_PAGE)

    return driver    

def endService(driver):
    driver.quit()
