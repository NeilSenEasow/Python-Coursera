---

Description
This Python script calculates the pay based on the number of hours worked and the hourly rate, accounting for overtime.

Usage
1. Ensure Python is installed on your system.
2. Copy the code into a Python file.
3. Save it with a `.py` extension.
4. Run the script.
5. Input the number of hours worked when prompted.
6. Input the hourly rate when prompted.
7. The script calculates and outputs the total pay based on the provided inputs.

Functionality
- The script defines a function `computepay` that takes two parameters: `h` (hours worked) and `r` (hourly rate).
- If the hours worked are 40 or fewer, the function calculates the pay by multiplying the hours worked by the hourly rate.
- If the hours worked exceed 40, the function calculates the pay by adding the pay for the first 40 hours at the regular rate and the pay for the remaining hours at 1.5 times the regular rate.
- The user is prompted to input the hours worked and the hourly rate, and the script calls the `computepay` function to calculate the total pay.
- The calculated pay is then printed to the console.

---

Quesition
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function
