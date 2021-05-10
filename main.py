#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user input their age and determine
#   if they're able to date the grandma's grandchild


def main():
    # this function lets the user pick input their age determine
    #   if they're able to date the grandma's grandchild

    # input
    age = input("Enter your age: ")

    # process & output
    try:
        age_int = int(age)

        if age_int > 40:
            print("\nYou are too old!")

        elif age_int < 25:
            print("\nYou are too young!")

        elif age_int >= 25 and age_int <= 40:
            print("\nYou may date my grandchild.")

    except Exception:
        print("\n{0} is not a valid input.".format(age))

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
