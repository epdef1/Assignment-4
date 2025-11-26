#!/usr/bin/env python3
"""
Created by: Erik
Created on: Nov 2025
This program checks if a person is eligible to vote in Canada.
"""


def main() -> None:
    """The main() function gets the user's age and tells them if they can vote."""
    try:
        # Input
        age = int(input("Enter your age: "))

        # Process + Output
        if age >= 18:
            print("You are eligible to vote in Canada.")
        elif age >= 0:
            print("You are NOT eligible to vote in Canada.")
        else:
            print("Age cannot be negative.")

    except ValueError:
        print("Invalid input! Please enter a number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
