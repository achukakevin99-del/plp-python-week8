# Personal Mini-Toolkit
# A menu-driven program with four tools: a guessing game, a to-do list,
# a calculator and a name formatter.

import random


# Tool 1: Number Guessing Game
# Picks a secret number from 1 to 20 and loops until the user guesses it,
# giving "too high" / "too low" hints using conditionals.
def guessing_game():
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess_text = input("Your guess: ").strip()
        if not guess_text.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print(f"{guess} is too low. Try higher!")
        elif guess > secret:
            print(f"{guess} is too high. Try lower!")
        else:
            print(f"Correct! You got it in {attempts} attempt(s). Well done!")
            break


# Tool 2: To-Do List
# Stores tasks in a list that grows and shrinks while the program runs.
# Uses a loop for its own sub-menu and a for loop to show the tasks.
def todo_list():
    print("\n--- To-Do List ---")
    tasks = []

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Back to main menu")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task == "":
                print("A task can't be empty.")
            else:
                tasks.append(task)
                print(f"Added: '{task}'. You now have {len(tasks)} task(s).")
        elif choice == "2":
            if len(tasks) == 0:
                print("Your list is empty - nothing to do!")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"  {number}. {task}")
        elif choice == "3":
            if len(tasks) == 0:
                print("Your list is empty - nothing to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"  {number}. {task}")
                number_text = input("Number of the task to remove: ").strip()
                if number_text.isdigit() and 1 <= int(number_text) <= len(tasks):
                    removed = tasks.pop(int(number_text) - 1)
                    print(f"Removed: '{removed}'. {len(tasks)} task(s) left.")
                else:
                    print("That's not a valid task number.")
        elif choice == "4":
            print("Returning to the main menu...")
            break
        else:
            print("Sorry, please choose 1, 2, 3 or 4.")


# Tool 3: Simple Calculator
# Asks for two numbers and an operation, then uses if / elif / else
# to calculate. It refuses to divide by zero.
def calculator():
    print("\n--- Simple Calculator ---")
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
    except ValueError:
        print("That wasn't a number. Back to the menu!")
        return

    operation = input("Operation (+, -, *, /): ").strip()

    if operation == "+":
        print(f"{first} + {second} = {first + second}")
    elif operation == "-":
        print(f"{first} - {second} = {first - second}")
    elif operation == "*":
        print(f"{first} * {second} = {first * second}")
    elif operation == "/":
        if second == 0:
            print("Oops! You can't divide by zero.")
        else:
            print(f"{first} / {second} = {first / second}")
    else:
        print("Sorry, I only know + - * and /.")


# Tool 4: Name Formatter
# Cleans up a name typed in any style and shows it capitalised,
# in uppercase, and as initials.
def name_formatter():
    print("\n--- Name Formatter ---")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()

    if first == "" or last == "":
        print("Please enter both a first and a last name.")
        return

    first = first.title()
    last = last.title()
    print(f"Formatted name: {first} {last}")
    print(f"Uppercase:      {first.upper()} {last.upper()}")
    print(f"Initials:       {first[0]}.{last[0]}.")
    print(f"Nice to meet you, {first}!")


# Main menu loop
# Shows the menu, runs the chosen tool, and repeats until the user quits.
def main():
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n=============================")
        print("   PERSONAL MINI-TOOLKIT")
        print("=============================")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")
        print("-----------------------------")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calculator()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thanks for using the toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' isn't on the menu. Please enter 1-5.")


main()
