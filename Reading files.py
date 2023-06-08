#First open the text file
employeefile=open("C:\\Coding\\Learn Python Beginner course\\employees.txt","r") 
#only read file
#w=write, a=append, r+ =read and write

print(employeefile.readable())
#Tells you if file is readable

#print(employeefile.read()) # prints info in file

#print(employeefile.readline())#reads first line = only 1 line
#print(employeefile.readline())#reads second

#print(employeefile.readlines()) #turns lines in text file into ana array
#print(employeefile.readlines()[1]) # prints second line only
for employee in employeefile.readlines():
    print(employee)
employeefile.close() #always close file