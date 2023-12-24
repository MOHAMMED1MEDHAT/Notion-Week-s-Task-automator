from datetime import datetime

#local imports
from config import TaskTypes
# from utils.taskXmlTempUtil import createTaskTemp

def getTasks(tasks):
    print("welcome to the task manager where you can add your tasks for the week")
    for idx,day in enumerate(tasks):
        dateNow=datetime.now().strftime('%b %d,20%y')
        nextDay=int(dateNow[4:6])+idx+1
        nextDayDate=dateNow[:4]+str(nextDay)+dateNow[6:]
        print(f"Enter tasks for nextDay which is ({nextDayDate})")
        continueToInput=True
        while continueToInput:
            name=input("please enter task name:")
            status=input("please enter task status (0 for not started,1 for in progress):")
            type=input("please enter task type :")
            if type not in TaskTypes:
                print("task type is not valid")
                continue

            print("do you want to add another task? (y/n)")
            answer=input()
            if answer=="n":
                continueToInput=False
            
            #for now we will add the task to the list and work on the xml later
            # tasks[day].append(createTaskTemp(name,status,str(TaskTypes.index(type))))
                
            tasks[day].append({"name":name,"status":status,"type":TaskTypes.index(type)})

    return tasks