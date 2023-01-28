# basic operations on lists
list1 = [1,2,3,4]
list2 = [11,12,13]
list = list1 + list2 # join lists
print(list)

# create a new list list3 based on the existing list1
print (id(list1))
list3 = list1 # not work. Why?
print (id(list3))
list3 = list1[:] # Its ok. 
print (id(list3))

for item in list: # iterating list items
    print (item)

list.insert(4,8) # adding an item at a specific location
print(list)

list.extend([100,101]) #adding at the end, 2 elements
print(list)

val = list.pop() #removes the last element and returns its value
print(val)
print(list)

val = list.pop(1) #removes the second element and returns its value
print(list)
print (list.index(13)) #returns element index with value '13'

print ( 13 not in list) #checks if 13 is not listed

print (list.count(8)) #counts how many '8' is on the list

list.sort(reverse=True) #sort descending lists
print (list)
list.reverse() #reverses the order of the list
print(list)
