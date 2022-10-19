#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 18, 2022
# This program asks for your age and
# grandparents tell you if you are
# allowed to date their grandchild

import math

zeroValue = 0;

def main():
    # input
    print("This program asks you for your age")
    print("grandparents tell you if you are")
    print("allowed to date their grandchild")
    print("")
    user_age_string = input("Enter your age: ")
    # user_age_int = user_age_string

    # process
    # checking that user_age_string is an int
    try:
        user_age_string = int(user_age_string)
    except ValueError:
        print("\n")
        print(("Please enter a valid number. {} is not valid.\n").format(user_age_string))
    finally:
        print("")

    # checking that user_age_int isn't zero
    if user_age_string == 0:
        print("Please do not enter zero.")

    # checking that user_age_int isn't negative
    if user_age_string < 0:
        print("Please do not enter a negative number or decimal.")

    # Output
    # checking to see if grandchild can be dated
    if user_age_string > 25 and user_age_string < 40:
        print("You are in the right age range. Congratulations :)")
    else:
        print("You are not in the right age range. Sorry :(")


if __name__ == "__main__":
    main()
