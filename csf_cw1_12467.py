print("Let's check if you get full mark from your CW")


def full_mark():
    print("You get full mark!")


def minus_10():
    print("You get minus 10 marks from overall mark but not below 40")


def zero_mark():
    print("Your mark is 0")


def deferral():
    print("You get deferral")


def answer1():
    ans1 = input("Did you upload your file on time? (y/n) \n > ")

    if ans1 == 'y':
        full_mark()
    elif ans1 == 'n':
        def answer2():
            ans2 = input("Have you uploaded within 24 hours? (y/n) \n > ")
            if ans2 == 'y':
                def answer2_1():
                    ans2_1 = input("Is there a valid reason? (y/n) \n > ")
                    if ans2_1 == 'n':
                        minus_10()
                    elif ans2_1 == 'y':
                        def answer2_2():
                            ans2_2 = input("Has your MC been accepted? (y/n) \n > ")
                            if ans2_2 == 'y':
                                full_mark()
                            elif ans2_2 == 'n':
                                minus_10()
                            else:
                                answer2_2()
                        answer2_2()
                    else:
                        answer2_1()
                answer2_1()
            elif ans2 == 'n':
                def answer3():
                    ans3 = input("Have you submitted it within 5 days? (y/n) \n > ")
                    if ans3 == 'n':
                        def answer3_1():
                            ans3_1 = input("Is there a valid reason? (y/n) \n > ")
                            if ans3_1 == 'n':
                                zero_mark()
                            elif ans3_1 == 'y':
                                def answer3_2():
                                    ans3_2 = input("Has your MC before specified deadline been accepted? (y/n) \n > ")
                                    if ans3_2 == 'y':
                                        deferral()
                                    elif ans3_2 == 'n':
                                        zero_mark()
                                    else:
                                        answer3_2()
                                answer3_2()
                            else:
                                answer3_1()
                        answer3_1()
                    elif ans3 == 'y':
                        def answer4():
                            ans4 = input("Is there a valid reason? (y/n) \n > ")
                            if ans4 == 'n':
                                zero_mark()
                            elif ans4 == 'y':
                                def answer4_1():
                                    ans4_1 = input("Has your MC(late submission option) been accepted? (y/n) \n > ")
                                    if ans4_1 == 'y':
                                        full_mark()
                                    elif ans4_1 == 'n':
                                        zero_mark()
                                    else:
                                        answer4_1()
                                answer4_1()
                            else:
                                answer4()
                    else:
                        answer3()
                answer3()
            else:
                answer2()
        answer2()
    else:
        answer1()


if __name__ == '__main__':
    answer1()