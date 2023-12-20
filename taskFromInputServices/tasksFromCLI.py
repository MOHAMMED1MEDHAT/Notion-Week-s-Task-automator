from config import TaskTypes
tasks={"sat":[],"sun":[],"mon":[],"tue":[],"wed":[],"thu":[],"fri":[]}

def getTasks():
    print("welcome to the task manager where you can add your tasks for the week")
    for day in tasks:
        print("enter tasks for "+day)
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
            tasks[day].append({"name":name,"status":status,"type":TaskTypes.index(type)})
    return tasks