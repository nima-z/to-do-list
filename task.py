from datetime import datetime


class Task(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date


dl_tasks = {}
w_tasks = {}
