import time

#local imports
from services.taskAutomationServices.utils.selenuimIntiatorUtil import startService,endService
from services.taskAutomationServices.utils.navigationFlowUtil import addTask

def createTasks(tasks):    
    #1 intiate selenium
    driver=startService()
    time.sleep(10)
    #2 run navigation flow
    for day in tasks:
        print(f"Processing day: {day}")
        for task in tasks[day]:
            print("inside inner loop")
            addTask(driver,day,task)
        print(f"finished adding tasks for {day}")
        #TODO: add a progress bar here
    #3 close selenium
    endService(driver)

def progressBar(progress,total):
    percent=100*(progress/float(total))
    bar='█'*int(percent)+'_'*(100-int(percent))
    print(f"\r | {bar} | {percent:.2f}%",end='\r')