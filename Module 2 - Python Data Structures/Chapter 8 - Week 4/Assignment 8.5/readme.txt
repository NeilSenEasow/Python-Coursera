---

Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python script file.
3. Run the script.
4. When prompted, enter the name of the file you want to process. If no file name is provided, the script will default to "mbox-short.txt".

Upon running, the script will open the specified file, iterate through its lines, extract email addresses from lines starting with "From", and print them. It will also print the total count of such lines.

Details

The script performs the following steps:

1. It prompts the user to enter the name of the file to be processed. If no file name is provided, it defaults to "mbox-short.txt".
2. It opens the specified file for reading.
3. It initializes a variable to count the lines with "From" as the first word.
4. It iterates through each line in the file.
5. For each line, it strips any trailing whitespace and splits it into words.
6. If the word "From" is found in the line, it prints the second word (which is assumed to be an email address) and increments the count.
7. If "From" is not found, it continues to the next line.
8. After processing all lines, it prints the total count of lines where "From" is the first word.

Note

Ensure that the specified file exists in the directory from which the script is executed. Additionally, the script assumes that email addresses are the second word on lines starting with "From". If the file format is different, the script may need to be adapted accordingly.

Question

Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt