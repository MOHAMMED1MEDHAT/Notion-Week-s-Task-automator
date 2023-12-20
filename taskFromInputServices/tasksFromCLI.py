def getTasks():
    tasks = []
    while True:
        task = input("Enter task: ")
        if task == "":
            break
        tasks.append(task)
    return tasks