from datetime import datetime
from task import *
import days


def create():
    mode = input("deadline or weekly?")
    if mode == "deadline":
        u_task = input("enter your task: \n")
        u_date = input("choose a date like --> dd.mm.yyyy: \n")

        # create object for class task
        dl_tasks[u_task] = Task(u_task, u_date)
        dl_tasks[u_task].display_done()

        # appending tasks and time to a dict
        days.deadlines[u_task] = u_date

    elif mode == "weekly":
        u_task = input("enter your task: \n")
        u_day = input('choose a day or choose multiple days seperated by ",": \n')

        # create object for class task
        w_tasks[u_task] = Task(u_task, u_day)
        w_tasks[u_task].display_done()

        # appending tasks and time to a dict
        list_of_u_day = u_day.split(",")
        for x in list_of_u_day:
            days.days_of_week[x].append(u_task)
