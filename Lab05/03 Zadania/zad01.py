# 1. Podaj listę z pocztą elektroniczną kilku użytkowników i wylosuj jeden z nich.
# data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i wylosuj jeden z nich.
import random
data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
i = random.randint(0,len(data)-1)
print(data[i])
k=0
while k < len(data)-1:
    if '@gmail.com' not in data[k]:
        data.pop(k)

    else:
        k+=1
i = random.randint(0,len(data)-1)
print(data[i])