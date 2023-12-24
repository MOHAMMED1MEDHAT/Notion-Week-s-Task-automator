from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import subprocess

#local imports
# from utils import xPathLocationsUtil
import config

def startService():
    #1-open chrome in debuging mode
    subprocess.run(f"chrome --remote-debugging-port={config.CHROME_DEBUGING_PORT}", shell=True)

    #2- connect to chrome
    chromeDebuggingServerLink=f"127.0.0.1:{config.CHROME_DEBUGING_PORT}"

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", chromeDebuggingServerLink)
    chrome_driver = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.get(config.NOTION_TASK_PAGE)

    return driver

def endService(driver):
    driver.quit()
