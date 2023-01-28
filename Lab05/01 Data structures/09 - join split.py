# how to join array elements and how to separate them (join, split)
list1 = ['John','Peter','Rob']
delimiter = ';'
output = delimiter.join(list1) # join list items
print(output)
list2 = output.split(delimiter) # split the string into list elements
print(list2)
