fname = input("Enter file name: ")
fr = open(fname,"r")
a = fr.readlines()

for line in a:
    line = line.rstrip()
    print(line.upper())
        