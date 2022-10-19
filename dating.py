#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 18, 2022
# This program asks for your age and
# grandparents tell you if you are
# allowed to date their grandchild

import math


def main():
    # input
    print("This program asks you for your age")
    print("grandparents tell you if you are")
    print("allowed to date their grandchild")
    print("")
    user_age_string = int(input("Enter your age: "))

    # process
    # checking that user_age_string is an integer
    try:
        user_age_int = int(user_age_string)
    except ValueError:
        print("\n")
        print("Please enter a valid number. ")
        print(("{} is not valid.\n").format(user_age_string))

    # checking that user_age_int isn't negative
    try:
        user_age_int > 0
    except:
        print("")
        print("Please do not enter a negative number.")

    # checking that user_age_int isn't zero
    try:
        user_age_int != 0
    except:
        print("")
        print("Please do not enter zero.")

    # Output
    # checking to see if grandchild can be dated
    if user_age_int > 25 and user_age_int < 40:
        print("You are in the right age range. Congratulations :)")
    else:
        print("You are not in the right age range. Sorry :(")


if __name__ == "__main__":
    main()
