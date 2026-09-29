# toolkit.py
# Personal Mini-Toolkit - a menu-driven program with four tools:
#   1. To-Do List   2. Number Guessing Game   3. Simple Calculator   4. Name Formatter

import random  # used by the guessing game to pick a secret number

# The to-do list is created BEFORE the main loop so the tasks
# are remembered every time the user comes back to the menu.
todo_list = []

print("Welcome to your Personal Mini-Toolkit!")

# ---------------------------------------------------------------
# MAIN MENU LOOP - keeps showing the menu until the user quits
# ---------------------------------------------------------------
while True:
    print("\n==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. To-Do List")
    print("2. Number Guessing Game")
    print("3. Simple Calculator")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ").strip()

    # -----------------------------------------------------------
    # TOOL 1: To-Do List
    # Lets the user add, remove and show tasks. The tasks live in
    # the todo_list list, which changes while the program runs.
    # -----------------------------------------------------------
    if choice == "1":
        print("\n--- To-Do List ---")
        while True:
            action = input("What now? (add / remove / show / back): ").strip().lower()

            if action == "add":
                task = input("Task to add: ").strip()
                if task == "":
                    print("You didn't type anything, so nothing was added.")
                else:
                    todo_list.append(task)
                    print(f"Added '{task}'. You now have {len(todo_list)} task(s).")

            elif action == "remove":
                task = input("Task to remove: ").strip()
                if task in todo_list:  # check first so .remove() never crashes
                    todo_list.remove(task)
                    print(f"Removed '{task}'. {len(todo_list)} task(s) left.")
                else:
                    print(f"'{task}' is not on your to-do list.")

            elif action == "show":
                if len(todo_list) == 0:
                    print("Your to-do list is empty. Nice and free!")
                else:
                    print("Your to-do list:")
                    number = 1
                    for task in todo_list:
                        print(f"  {number}. {task}")
                        number += 1

            elif action == "back":
                print("Going back to the main menu...")
                break

            else:
                print("Please type add, remove, show or back.")

    # -----------------------------------------------------------
    # TOOL 2: Number Guessing Game
    # The computer picks a number from 1 to 20 and the user gets
    # 5 tries. A loop repeats the guesses; conditionals give hints.
    # -----------------------------------------------------------
    elif choice == "2":
        print("\n--- Number Guessing Game ---")
        secret_number = random.randint(1, 20)
        max_attempts = 5
        attempts = 0
        won = False

        print(f"I'm thinking of a number between 1 and 20. You have {max_attempts} tries!")

        while attempts < max_attempts:
            guess_text = input(f"Guess #{attempts + 1}: ").strip()

            if not guess_text.isdigit():
                print("Please enter a whole number (that didn't use up a try).")
            else:
                guess = int(guess_text)
                attempts += 1

                if guess == secret_number:
                    print(f"Correct! You got it in {attempts} guess(es). Well done!")
                    won = True
                    break
                elif guess < secret_number:
                    print("Too low! Try a bigger number.")
                else:
                    print("Too high! Try a smaller number.")

        if not won:
            print(f"Out of tries! The number was {secret_number}. Better luck next time!")

    # -----------------------------------------------------------
    # TOOL 3: Simple Calculator
    # Asks for two numbers and an operation, then uses
    # if / elif / else to work out and print the answer.
    # -----------------------------------------------------------
    elif choice == "3":
        print("\n--- Simple Calculator ---")
        try:
            first = float(input("First number: "))
            operator = input("Operation (+, -, *, /): ").strip()
            second = float(input("Second number: "))

            if operator == "+":
                print(f"{first:g} + {second:g} = {first + second:g}")
            elif operator == "-":
                print(f"{first:g} - {second:g} = {first - second:g}")
            elif operator == "*":
                print(f"{first:g} * {second:g} = {first * second:g}")
            elif operator == "/":
                if second == 0:
                    print("Oops! You can't divide by zero.")
                else:
                    print(f"{first:g} / {second:g} = {first / second:g}")
            else:
                print(f"Sorry, '{operator}' is not an operation I know.")
        except ValueError:
            # float() fails if the user types letters instead of a number
            print("That wasn't a valid number. Please try again from the menu.")

    # -----------------------------------------------------------
    # TOOL 4: Name Formatter
    # Takes a first and last name and shows it in a few tidy ways.
    # -----------------------------------------------------------
    elif choice == "4":
        print("\n--- Name Formatter ---")
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()

        if first_name == "" or last_name == "":
            print("Please enter both a first name and a last name.")
        else:
            full_name = f"{first_name.title()} {last_name.title()}"
            initials = first_name[0].upper() + last_name[0].upper()
            letters = len(first_name) + len(last_name)
            print(f"Nicely formatted: {full_name}")
            print(f"In capitals:      {full_name.upper()}")
            print(f"Initials:         {initials}")
            print(f"Letters in name:  {letters}")

    # -----------------------------------------------------------
    # QUIT: say goodbye and leave the main loop
    # -----------------------------------------------------------
    elif choice == "5":
        print("\nThanks for using the toolkit. Goodbye!")
        break

    # -----------------------------------------------------------
    # ANYTHING ELSE: a polite message - the program never crashes
    # -----------------------------------------------------------
    else:
        print(f"\nSorry, '{choice}' is not on the menu. Please enter a number from 1 to 5.")
