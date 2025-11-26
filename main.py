#!/usr/bin/env python3
"""
Created by: Erik
Created on: Nov 25
This program checks if a number is even or odd.
"""


def main() -> None:
    """The main() function gets a number and tells the user if it is even or odd."""
    # Input
    user_number = int(input("Enter an integer: "))

    # Process + Output
    if user_number % 2 == 0:
        print(f"{user_number} is even.")
    else:
        print(f"{user_number} is odd.")

    print("\nDone.")


if __name__ == "__main__":
    main()
