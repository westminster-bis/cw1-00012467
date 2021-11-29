import datetime

def upload_date():
    answer = input("Input the exact date time when you uploaded your CW (YY/MM/DD/hour/minute) \n > ")
    thedate = list(map(int,answer.split('/')))
    uploaddate = datetime.datetime(thedate[0], thedate[1], thedate[2], thedate[3], thedate[4])

    answer = input("Input the exact date and time when the deadline for your CW was (YY/MM/DD/hour/minute) \n > ")
    thedate = list(map(int, answer.split('/')))
    deadline = datetime.datetime(thedate[0], thedate[1], thedate[2], thedate[3], thedate[4])

    difference = deadline - uploaddate
    date1 = datetime.datetime(2021,11,26,23,59)
    date2 = datetime.datetime(2021, 11, 27, 23, 59)
    day_dif = date1 - date2
    if deadline < uploaddate:
        if difference >= day_dif:
            print("Difference is between 24 hours")
        elif difference < day_dif:
            print("Difference is not between 24 hours")
    elif deadline >= uploaddate:
        print("W")

if __name__ == '__main__':
    upload_date()