import datetime

def upload_date():
    answer = input("Input the exact date time when you uploaded your CW (YY/MM/DD/hour/minute) \n > ")
    thedate = list(map(int,answer.split('/')))
    uploaddate = datetime.datetime(thedate[0], thedate[1], thedate[2], thedate[3], thedate[4])

    answer = input("Input the exact date and time when the deadline for your CW was (YY/MM/DD/hour/minute) \n > ")
    thedate = list(map(int, answer.split('/')))
    deadline = datetime.datetime(thedate[0], thedate[1], thedate[2], thedate[3], thedate[4])

if __name__ == '__main__':
    upload_date()