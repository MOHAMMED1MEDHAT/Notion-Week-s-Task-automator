#local imports
from services.taskFromInputServices import tasksFromCLI
from services.taskAutomationServices import taskCreationService
from services.tasksContentServices.tasksDict import tasks

if __name__=="__main__":
    #1) get the tasks from the cli
    # tasks=tasksFromCLI.getTasks(tasks)
    # print(tasks)
    #2) add the tasks to notion
    taskCreationService.createTasks(tasks)
    #TODO:3) show a progress bar
    #TODO:4) add a logger
    #TODO:5) add mail service notification

