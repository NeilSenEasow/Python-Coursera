# Prompt for file name
file_name = input("Enter file name: ")

# Initialize variables
count = 0
total = 0

try:
    # Open the file
    with open(file_name, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line starts with 'X-DSPAM-Confidence:'
            if line.startswith('X-DSPAM-Confidence:'):
                # Extract the floating point value from the line
                colon_pos = line.find(':')
                value = float(line[colon_pos + 1:])
                
                # Update count and total
                count += 1
                total += value

    # Compute the average
    if count > 0:
        average = total / count
        print("Average spam confidence:", average)
    else:
        print("No lines found matching the pattern.")

except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except PermissionError:
    print("Error: Permission denied. You don't have permission to access the file.")
except Exception as e:
    print("An error occurred:", e)
