from datetime import datetime


class Task(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display_done(self):
        print(f"You created task '{self.name}' for '{self.date}'")

    def edit(self, new_date):
        self.date = new_date
        print(f"You changed {self.name}'s schedule to {self.date}")

    def delete(self):
        print(f"You deleted {self.name}")


dl_tasks = {}
w_tasks = {}
