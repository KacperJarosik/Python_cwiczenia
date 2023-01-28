# app04
# Mamy przykładową zmienną data: data = ['jeden','dwa','trzy','cztery','pięć','sześć']
data = ['jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć']
# Wyświetl w kolejnych linijkach kolejną pozycję w postaci ciągu znaków np.
# jeden
#  j
#  e
#  d
#  e
#  n
# ...
a = int(0)
while a < 6:
    for letter in data[a]:
        print(' ', letter)
    print('...\n')
    a += 1
