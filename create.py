from datetime import datetime
from task import *


def create():
    mode = input("deadline or weekly?")
    if mode == "deadline":

        u_task = input("enter your task: \n")
        u_date = input("choose a date: \n")

        date = datetime.strptime(u_date, "%d.%m.%Y")
        # day_of_week = date.strftime("%A")
        # create object for class
        dl_tasks[u_task] = Task(u_task, u_date)

    elif mode == "weekly":
        u_task = input("enter your task: \n")
        u_day = input("choose a day: \n")

        w_tasks[u_task] = Task(u_task, u_day)

        pass
