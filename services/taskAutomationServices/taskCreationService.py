from utils.selenuimIntiatorUtil import startService,endService
from utils.navigationFlowUtil import addTask

def createTasks(tasks):    
    #1 intiate selenium
    driver=startService()
    #2 run navigation flow
    for day in tasks:
        for task in tasks[day]:
            addTask(driver,day,task)
        print(f"finished adding tasks for {day}")
        #TODO: add a progress bar here

def progressBar(progress,total):
    percent=100*(progress/float(total))
    bar='█'*int(percent)+'_'*(100-int(percent))
    print(f"\r | {bar} | {percent:.2f}%",end='\r')