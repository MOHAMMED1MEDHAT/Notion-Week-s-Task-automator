from datetime import datetime

#local imports
from services.taskFromInputServices import tasksFromCLI
from services.tasksContentServices.tasksDict import tasks

if __name__=="__main__":
    #get the tasks from the cli
    tasks=tasksFromCLI.getTasks(tasks)
    print(tasks)
    # # print(datetime.fromisocalendar().strftime("%b %d,20%y"))
    # print(datetime.now())
