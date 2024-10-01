import datetime

myfile = open(r"C:\Users\ethan\OneDrive\Desktop\today.txt")

year = myfile.readline()
month = myfile.readline()
day = myfile.readline()


print(year, month, day)
