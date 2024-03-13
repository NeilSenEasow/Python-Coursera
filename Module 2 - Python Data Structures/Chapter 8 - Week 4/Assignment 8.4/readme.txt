---

Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python script file.
3. Run the script.
4. When prompted, enter the name of the file you want to process.

Upon running, the script will open the specified file, extract unique words from its content, sort them alphabetically, and print the sorted list.

Details

The script performs the following steps:

1. It prompts the user to enter the name of the file to be processed.
2. It initializes an empty list to store unique words.
3. It attempts to open the specified file and handle any potential errors such as file not found.
4. It reads all lines from the file and splits each line into words.
5. It iterates through each word, checking if it is not already in the list of unique words. If not, it appends it to the list.
6. After processing all words, it sorts the list of unique words alphabetically.
7. It prints the sorted list of unique words.

Note

Ensure that the specified file exists in the directory from which the script is executed. If the file contains non-alphanumeric characters as part of word separation, further processing may be required.

Question 

Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt