import task
import datetime
import create
import edit
import review


tasks = {}
while True:  # Choose a mode
    u_input = input("Create, Edit, Review, Exit:\n")
    # mode : Create
    if u_input.lower() == "create":
        create.Create()
    elif u_input.lower() == "edit":
        edit.Edit()
    elif u_input.lower() == "review":
        review.Review()
    elif u_input.lower() == "exit":
        break
