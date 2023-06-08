lucky_numbers=[25,42,4,23,16,8]
friends=["Kevin","Karen","Jim","Jim","Oscar","Toby"]
print(friends)

friends.count("Jim") #Counts how many times item is in list
print(friends)

friends.remove("Jim") #Removes item in list
print(friends)

print(friends.index("Karen")) # Tells me where item is, no item=error

friends.sort() #sorts into alphabetical order
print(friends)

print(lucky_numbers)

lucky_numbers.sort() #sorts into ascending order
print(lucky_numbers)

lucky_numbers.reverse() #Reverses order of list
print(lucky_numbers)

friends.extend(lucky_numbers) #lets you add 2 lists together
print(friends)

friends.append("Creed") #adds to list
print(friends)

friends2=friends.copy() #copy items in a list into another list
print(friends2)

friends.insert(1,("Kelly")) #Adds B to position A
print(friends)

friends.remove("Jim") #Removes item in list
print(friends)

friends.pop() #Takes off last item from list
print(friends)

friends.clear() #clears list
print(friends)