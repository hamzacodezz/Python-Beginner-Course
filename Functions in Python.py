def sayhi(): #Create a function
    print("Hello User")

sayhi()

#Parameters - the things in () - additional info
def sayhi(name,age): #the parameters
    print("Hello "+name+", you are "+str(age))

sayhi("Dave",80) #Dave and 80 the parameters

#Return Statements
#Used to get something back from a function - return info

def cube(num):
    return num*num*num

print(cube(3))

#Alternatively
result=cube(4)
print(result)