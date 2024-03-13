fname = input("Enter name of file: ")
a=[]
try:
    fr = open(fname,"r")
    line = fr.readlines()
    for i in line:
        word = i.split()
        for i in word:
            if i not in a:
                a.append(i)
    a.sort()
    print(a)
except FileExistsError:
    print("File not found. Please enter a valid file name.")
except:
    print("Error")