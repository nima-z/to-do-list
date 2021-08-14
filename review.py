import days


def Review():
    u_choice = input("review deadlines or week? \n")
    if u_choice == "deadline":
        print(days.deadlines)
    elif u_choice == "week":
        print(days.weekly)
