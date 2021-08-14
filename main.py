import task
import create
import datetime

tasks = {}
while True:  # Choose a mode
    u_input = input("Create, Edit, Review, Exit:\n")
    # mode : Create
    if u_input.lower() == "create":
        create.create()
    elif u_input.lower() == "edit":
        pass
    elif u_input.lower() == "review":
        pass
    elif u_input.lower() == "exit":
        break
