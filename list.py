#create an empty list my_list
my_list = []
#Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#Insert value at a specific position: Adds 15 at the second position (index)
my_list.insert(1,15)
print(my_list)

#Extend my_list with another list: [50, 60, 70]
my_list.extend([50,60,70])
print(my_list)

#Remove the last element from my_list.
my_list.pop()
print(my_list)

#3Sort my_list in ascending order.
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("index_of_30:", index_of_30)