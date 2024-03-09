---

Description
This Python script prompts the user to input numbers until they enter "done". It then finds and prints the largest and smallest numbers from the provided inputs.

Usage
1. Ensure Python is installed on your system.
2. Copy the code into a Python file.
3. Save it with a `.py` extension.
4. Run the script.
5. Input numbers one by one when prompted. To finish input, enter "done".
6. The script will calculate and display the largest and smallest numbers from the provided inputs.

Functionality
- The script initializes variables `largest` and `smallest` to None.
- It creates an empty list called `the_list` to store the user's inputs.
- The script enters a while loop that continues until the user enters "done".
- Inside the loop, it prompts the user to input a number. If the input is not a valid integer, it displays an error message.
- The valid numbers are added to the `the_list`.
- After the user finishes input, the script iterates through the numbers in `the_list` to find the largest and smallest numbers.
- It prints the largest and smallest numbers to the console.

Issues
The script contains hardcoded lists `[7, 2, 10, 4]` for finding the largest and smallest numbers. It does not use the user's input for this purpose.

---

Question
 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.