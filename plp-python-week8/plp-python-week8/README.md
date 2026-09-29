# Week 8 Final Project: Personal Mini-Toolkit

## What it does

A menu-driven Python program that bundles four small tools into one toolkit:

1. **To-Do List** — add, remove and show tasks (the list is remembered while the program runs).
2. **Number Guessing Game** — guess the computer's secret number from 1 to 20 in 5 tries, with "too low / too high" hints.
3. **Simple Calculator** — add, subtract, multiply or divide two numbers (and it won't crash on divide-by-zero or typos).
4. **Name Formatter** — turns a first and last name into a tidy version, capitals, initials and a letter count.

The menu keeps coming back after each tool until you choose **5. Quit**, and it politely handles choices that aren't on the menu.

## Files

- `toolkit_plan.txt` — my plan: the tools, the exact menu text, and the concepts each tool uses.
- `toolkit.py` — the toolkit program.
- `screenshots/` — screenshots of the menu (including an invalid choice) and each tool running.

## How to run it

1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run: `python toolkit.py` (or `python3 toolkit.py` on Mac/Linux).
4. Type a number from the menu and press Enter.

## Reflection

<!-- Rewrite this reflection in your own words so it matches your real experience. -->

The hardest part was making the to-do list remember its tasks between visits to the menu. I had to create the list before the main loop so it wasn't reset every time the menu came back. The bug that took longest to fix was the guessing game: at first a typo like "abc" crashed the program, and later it wrongly used up one of the player's tries. Using `.isdigit()` before converting to an integer fixed both problems. Planning in `toolkit_plan.txt` first really did make the build faster, because I already knew the menu text and which tool needed which concept. With one more week I would save the to-do list to a file so it survives after quitting, and add a countdown timer and a high-score tracker for the guessing game.
