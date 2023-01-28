animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # create new list
print(animals)

animals[1:3] = ["cat"]  # replace 2 items -- "lion" and "tiger" with one item -- "cat"
print(animals)

animals[1:3] = []  # remove 2 items -- "cat" and "giraffe" from the list
print(animals)

# Clear animals list.
# Hint: Use assignment to an empty list [].
# animals = [] ???
# animals[:]=[]
animals.clear()
pass  # 1
#
print(animals)

# example2
dane = ['Peter', 'John']
print(dane)  # ['Peter', 'John']
dane[1] = ['Rob', 'Newman']
print(dane)  # ['Peter', ['Rob', 'Newman']]

# Print 'Rob'
pass  # 2
print(dane[1][0])
