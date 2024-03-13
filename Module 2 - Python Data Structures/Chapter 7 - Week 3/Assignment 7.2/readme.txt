---

Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python script file.
3. Run the script.
4. When prompted, enter the name of the file containing spam confidence data.

Upon running, the script will open the specified file, iterate through its lines, extract the spam confidence values, calculate the average, and print the result.

Details

The script performs the following steps:

1. It prompts the user to enter the name of the file to be processed.
2. It initializes variables to keep track of the count of spam confidence values and their total.
3. It attempts to open the specified file and handle any potential errors such as file not found or permission denied.
4. It iterates through each line in the file, checking if it starts with the pattern 'X-DSPAM-Confidence:'.
5. If a matching line is found, it extracts the floating-point value after the colon, updates the count and total, and continues.
6. After processing all lines, it computes the average spam confidence if there are lines matching the pattern and prints it. If no matching lines are found, it prints a message indicating this.
7. If any unexpected errors occur during execution, it catches and handles them, printing an error message.

Note

Ensure that the specified file exists in the directory from which the script is executed and follows the expected format for spam confidence data.

Question

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.