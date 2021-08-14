from datetime import datetime


class Task(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display_done(self):
        print(f"You created task '{self.name}' for '{self.date}'")


dl_tasks = {}
w_tasks = {}
