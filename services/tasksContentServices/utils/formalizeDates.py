from datetime import datetime


def formalizeDate(tasks):
    #set date of each date
    for day in tasks.keys:
        for task in tasks[day]:
            task["date"]=""