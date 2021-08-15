import days


def Review():
    u_choice = input("review deadlines or weekly? \n")
    if u_choice == "deadlines" or u_choice == "deadline":
        print(days.deadlines)
    elif u_choice == "weekly" or u_choice == "week":
        print(days.weekly)
