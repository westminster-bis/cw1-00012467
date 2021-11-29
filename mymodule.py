import datetime


def full_mark():
    print("You get full mark!")


def minus_10():
    print("You get minus 10 marks from overall mark but not below 40")


def zero_mark():
    print("Your mark is 0")


def deferral():
    print("You get deferral")


def mc_claim1():
    answer = input("Has your MC been accepted? (y/n) \n > ")
    if answer == 'y':
        full_mark()
    elif answer == 'n':
        minus_10()
    else:
        mc_claim1()


def mc_claim2():
    answer = input("Has your MC been accepted? (y/n) \n > ")
    if answer == 'y':
        full_mark()
    elif answer == 'n':
        zero_mark()
    else:
        mc_claim2()


def within_24():
    print("You have uploaded within 24 hours after the deadline. You got Late Submission")
    answer = input("Is there a valid reason for your Late Submission? (y/n) \n > ")
    if answer == 'y':
        mc_claim1()
    elif answer == 'n':
        minus_10()
    else:
        within_24()


def within_5days():
    print("You have uploaded within 5 days after the deadline. You got Late Submission")
    answer = input("Is there a valid reason for your Late Submission? (y/n) \n > ")
    if answer == 'y':
        mc_claim2()
    elif answer == 'n':
        zero_mark()
    else:
        within_5days()

def upload_date():
    answer = list(map(int,(input("Input the exact date time when you uploaded your CW (YY/MM/DD/hour/minute) \n > ").split('/'))))
    uploaddate = datetime.datetime(answer[0], answer[1], answer[2], answer[3], answer[4])

    answer = list(map(int,(input("Input the exact date and time when the deadline for your CW was (YY/MM/DD/hour/minute) \n > ").split('/'))))
    deadline = datetime.datetime(answer[0], answer[1], answer[2], answer[3], answer[4])

    difference = deadline - uploaddate

    date1 = datetime.datetime(2021, 11, 26, 23, 59)
    date2 = datetime.datetime(2021, 11, 27, 23, 59)

    date3 = datetime.datetime(2021, 11, 21, 23, 59)
    date4 = datetime.datetime(2021, 11, 26, 23, 59)

    day_dif = date1 - date2
    day_dif2 = date3 - date4


    if deadline < uploaddate:
        if difference >= day_dif:
            within_24()
        elif difference < day_dif:
            if day_dif > difference >= day_dif2:
                within_5days()
            else:

    elif deadline >= uploaddate:
        full_mark()
if __name__ == '__main__':
    upload_date()