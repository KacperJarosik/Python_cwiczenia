# app07
# zaimportuj moduł random poleceniem - import random
import random
from typing import List

# wybierz losowo liczbę całkowitą od 0 do 100 - funkcja randinit() oraz randrange() (jaka jest różnica między funkcjami)
print(random.randint(0, 100))
# dla calkowitych^^
print(random.randrange(0, 100))
# wybierz losowo wartość z tablicy data = ['jeden','dwa','trzy','cztery','pięć','sześć'] - funkcja choice()
data = ['jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć']
print(random.choice(data))
# wybierz losowo liczbę od 0 do 1 - funkcja random()
print(random.random())
