print("Let's check if you get full mark from your CW")


def full_mark():
    print("You get full mark!")


def minus_10():
    print("You get minus 10 marks from overall mark but not below 40")


def zero_mark():
    print("Your mark is 0")


ans1 = input("Did you upload your file on time? (y/n) \n > ")


if ans1 == 'y':
    full_mark()
elif ans1 == 'n':
    ans2 = input("Have you uploaded within 24 hours? (y/n) \n > ")
    if ans2 == 'y':
        ans3 = input("Is there a valid reason? (y/n) \n > ")
        if ans3 == 'n':
            minus_10()
        elif ans3 == 'y':
            ans3_1 = input("Have your MC been accepted? (y/n) \n > ")
            if ans3_1 == 'y':
                full_mark()


