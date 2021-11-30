import datetime  # imports datetime module to work with dates and time


def full_mark():  # function that prints certain phrase
    print("You get full mark!")


def minus_10():  # function that prints certain phrase
    print("You get minus 10 marks from overall mark but not below 40")


def zero_mark():  # function that prints certain phrase
    print("Your mark is 0")


def deferral():  # function that prints certain phrase
    print("You get deferral")


def mc_claim1():  # first version of MC claim algorithm
    answer = input("Has your MC been accepted? (y/n) \n > ")
    if answer == 'y':
        full_mark()
    elif answer == 'n':
        minus_10()
    else:
        mc_claim1()


def mc_claim2():  # second version of MC claim algorithm
    answer = input("Has your MC been accepted? (y/n) \n > ")
    if answer == 'y':
        full_mark()
    elif answer == 'n':
        zero_mark()
    else:
        mc_claim2()


def mc_claim3():  # third version of MC claim algorithm
    answer = input("Has your MC been accepted? (y/n) \n > ")
    if answer == 'y':
        deferral()
    elif answer == 'n':
        zero_mark()
    else:
        mc_claim3()


def within_24():  # function is called if the date difference between deadline and upload time is within 24 hours
    print("You have uploaded within 24 hours after the deadline. You got Late Submission")
    answer = input("Is there a valid reason for your Late Submission? (y/n) \n > ")
    if answer == 'y':
        mc_claim1()
    elif answer == 'n':
        minus_10()
    else:
        within_24()


def within_5days():  # function is called if the date difference between deadline and upload time is within 5 days
    print("You have uploaded within 5 days after the deadline. You got Late Submission")
    answer = input("Is there a valid reason for your Late Submission? (y/n) \n > ")
    if answer == 'y':
        mc_claim2()
    elif answer == 'n':
        zero_mark()
    else:
        within_5days()


def out_5days():  # function is called if the CW was not uploaded within 5 days after the deadline
    print("You have not uploaded within 5 days after the deadline.")
    answer = input("Is there a valid reason for this? (y/n) \n > ")
    if answer == 'y':
        mc_claim3()
    elif answer == 'n':
        zero_mark()
    else:
        out_5days()


def upload_date():
    #  takes as input date and time and converts it into int array
    answer = list(map(int, (input("Input the exact date and time when you uploaded the CW(YY/MM/DD/hour/minute) \n > ").split('/'))))
    uploaddate = datetime.datetime(answer[0], answer[1], answer[2], answer[3], answer[4])

    answer = list(map(int, (input("Input the exact date and time of deadline for your CW (YY/MM/DD/hour/minute) \n > ").split('/'))))
    deadline = datetime.datetime(answer[0], answer[1], answer[2], answer[3], answer[4])

    #  saves difference between deadline and upload time into a variable
    difference = deadline - uploaddate

    #  made to store 1 day and 5 days differences
    day_dif = -datetime.timedelta(days=1)
    day_dif2 = -datetime.timedelta(days=5)

    if deadline < uploaddate:  # checks if the cw was not uploaded in time
        if difference >= day_dif:  # checks if it was uploaded within 24 hours after deadline
            within_24()
        elif difference < day_dif:
            if day_dif > difference >= day_dif2:  # checks if it was uploaded within 5 days after deadline
                within_5days()
            else:
                out_5days()
    elif deadline >= uploaddate:  # checks if the cw was uploaded in time
        full_mark()