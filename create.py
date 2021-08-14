from datetime import datetime
from task import *
import days


def Create():
    mode = input("deadline or weekly?")
    if mode == "deadline":
        u_task = input("enter your task: \n")
        u_date = input("choose a date like --> dd.mm.yyyy: \n")

        # create object for class task
        dl_tasks[u_task] = Task(u_task, u_date)
        dl_tasks[u_task].display_done()

        # appending tasks and time to a dict
        days.deadlines[u_task] = u_date
        print(days.deadlines)

    elif mode == "weekly":
        u_task = input("enter your task: \n")
        u_day = input('choose a day or choose multiple days seperated by ",": \n')

        # create object for class task
        w_tasks[u_task] = Task(u_task, u_day)
        w_tasks[u_task].display_done()

        # appending tasks and time to a dict
        list_of_u_day = u_day.split(",")
        for x in list_of_u_day:
            index_x = days.days_of_week_str.index(x)
            days.days_of_week[index_x].append(u_task)
