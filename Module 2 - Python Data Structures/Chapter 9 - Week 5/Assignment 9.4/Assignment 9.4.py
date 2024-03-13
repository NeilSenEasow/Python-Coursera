# Initialize an empty dictionary to store sender's mail addresses and their counts
sender_counts = {}

# Open the file mbox-short.txt
with open("mbox-short.txt", "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Check if the line starts with 'From '
        if line.startswith('From '):
            # Split the line into words and extract the sender's email address (second word)
            sender = line.split()[1]
            # Update the count for the sender in the dictionary
            sender_counts[sender] = sender_counts.get(sender, 0) + 1

# Initialize variables to keep track of the most prolific committer
max_sender = None
max_count = 0

# Iterate through the dictionary to find the sender with the most messages
for sender, count in sender_counts.items():
    if count > max_count:
        max_sender = sender
        max_count = count

# Print the most prolific committer and their message count
print(max_sender,max_count)

