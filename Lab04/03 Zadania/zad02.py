# 2. Uzupełnij listę do 10 adresów i posortuj ją rosnąco po nazwie. Listę uzupełniamy z klawiatury i spradzamy ile jest elementów listy.
# Nie dodajemy adresu, który już istnieje.
import random

data = ['user3@gmail.com', 'user2@gmail.com', 'user2@interia.com', 'user1@gmail.com', 'user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i posortuj ją rosnąco po nazwie.
data += ['user4@gmail.com', 'user5@gmail.com', 'user6@gmail.com', 'user7@gmail.com', 'user8@gmail.com']
k = 0
while k < len(data) - 1:
    if '@gmail.com' not in data[k]:
        data.pop(k)

    else:
        k += 1
data = sorted(data)
i = random.randint(0, len(data) - 1)
print(data[i])
