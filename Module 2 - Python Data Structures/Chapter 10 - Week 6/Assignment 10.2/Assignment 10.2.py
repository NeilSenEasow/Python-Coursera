fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

hours = dict()  # Dictionary to store counts for each hour

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

# Convert dictionary items into a list of tuples and sort by hour
sorted_hours = sorted(hours.items())

# Print the sorted counts by hour
for hour, count in sorted_hours:
    print(hour, count)
