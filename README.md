# Personal Mini-Toolkit

## What it does
A menu-driven Python program with four tools that keeps running until you choose Quit:
1. **Number Guessing Game** – guess a secret number from 1 to 20 with higher/lower hints.
2. **To-Do List** – add, view and remove tasks stored in a list.
3. **Simple Calculator** – add, subtract, multiply or divide two numbers (with a divide-by-zero check).
4. **Name Formatter** – tidies a name into proper case, uppercase and initials.

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. In a terminal, go to the project folder and run:
   ```
   python toolkit.py
   ```
4. Type a number from the menu and press Enter.

## Files
- `toolkit_plan.txt` – my plan
- `toolkit.py` – the program
- `screenshots/` – the menu (including an invalid choice) and each tool running

## Reflection
EDIT THIS TO MATCH YOUR OWN EXPERIENCE (5–8 sentences). Example:
The hardest part was combining everything into one program, because each tool needed its own loop or conditionals without breaking the main menu. The bug that took longest to fix was in the to-do list, where I was removing the wrong task because list positions start at 0 but I displayed numbers starting at 1. I fixed it by subtracting 1 from the number the user typed. Planning in `toolkit_plan.txt` first made the build much faster. I also learned to handle bad input, like letters instead of numbers, so the program doesn't crash. With one more week I would save the to-do list to a file so tasks are kept between runs. I would also add a countdown timer and a high-score tracker for the guessing game.
