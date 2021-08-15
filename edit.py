import days
import task


def Edit():
    u_decide = input("You want to edit deadline or weekly?")

    if u_decide == "deadline":
        print(f"Your deadlines are {days.deadlines}")
        which_dl = input("which deadline do you want to edit?")

        if which_dl in days.deadlines:
            u_edit = input("edit (date) or delete?")

            if u_edit == "edit":
                new_date = input("set new date")
                task.dl_tasks[which_dl].edit(new_date)
                days.deadlines[which_dl] = new_date

            elif u_edit == "delete":
                task.dl_tasks[which_dl].delete()
                del task.dl_tasks[which_dl]
                del days.deadlines[which_dl]
        else:
            print("There is no match deadline in your schedule")

    elif u_decide == "weekly":
        print(f"Your weekly is {days.weekly}")

        u_edit = input("edit (days) or delete?")

        if u_edit == "edit":
            which_w = input("which weekly item do you want to edit?")

            new_day = input("choose new day or days (devided by ',')")
            task.w_tasks[which_w].edit(new_day)

            for x in days.days_of_week:
                if which_w in x:
                    x.remove(which_w)

            list_of_u_day = new_day.split(",")
            for i in list_of_u_day:
                index_i = days.days_of_week_str.index(i)
                days.days_of_week[index_i].append(which_w)

        elif u_edit == "delete":
            which_w = input("which weekly item do you want to edit?")

            task.w_tasks[which_w].delete()
            del task.w_tasks[which_w]
            for w in days.days_of_week:
                if which_w in w:
                    w.remove(which_w)

        else:
            print("There is no match deadline in your schedule")
