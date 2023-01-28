animals = ["elephant", "lion", "tiger", "giraffe"]  # create new list
print(animals)

animals += ["monkey", "dog"]    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)

#Replace "dino" with "dinosaur" in the animals list.
#Hint : Use indexing operation and assignment.
pass		
#
for x in range(len(animals)):
    if animals[x]=='dino':
        animals[x]='dinozaur'
print(animals)
