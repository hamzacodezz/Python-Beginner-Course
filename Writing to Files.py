# employeefile=open("C:\\Coding\\Learn Python Beginner course\\employees.txt","a") #adds to file
# employeefile.write("Toby - Human Resources")#writes to file
# employeefile.write("\nKelly - Customer Service")
# employeefile.close()

#using w overwrites everything in the file - deletes everything
#using w can alsp be used to create a new file

employeefile=open("C:\\Coding\\Learn Python Beginner course\\employee1.txt","w")
employeefile.write("\nKelly - Customer Service")
employeefile.close()

# employeefile2=open("C:\\Coding\\Learn Python Beginner course\\index.html","w")
# employeefile2.write("<p>This is HTML</p>")
# employeefile2.close()