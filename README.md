# Binary Guesser

## Overview
This project is an algorithmic demonstration of the Binary Search principle. Unlike a linear search, which checks every possibility, this script uses a divide-and-conquer strategy to narrow down the target number to a range of 1 to 25, significantly reducing the number of attempts required to reach the correct result.

## Technical Stack
- Language: Python 3.x
- Core Concepts:
    - Binary Search Algorithm
    - While-loop state management
    - Floor division for midpoint calculation
    - Conditional branching (if-elif-else)

## Logic and Efficiency
The script operates on a logarithmic scale. By calculating the midpoint between the 'low' and 'high' boundaries and adjusting those boundaries based on user feedback (Higher/Lower), the system eliminates half of the remaining possibilities with every guess.

## How To Run
1. Ensure Python is installed on your system.
2. Clone the repository.
3. Run the script via terminal:
   python binary_guesser.py
4. Follow the on-screen prompts to provide feedback (H, L, or C) to the computer.
