from services.taskAutomationServices.utils.selenuimIntiatorUtil import startService

def createTasks(tasks):    
    #1 intiate selenium
    startService(tasks)

def progressBar(progress,total):
    percent=100*(progress/float(total))
    bar='█'*int(percent)+'_'*(100-int(percent))
    print(f"\r | {bar} | {percent:.2f}%",end='\r')