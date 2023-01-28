# 3. Dana jest lista (można dodać dowolną o dowolnej liczbie elementów):
lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3, 1, -1, -2, 21]
# Znajdz wszystkie (łącznie z wykorzystanymi wcześniej) trzy kolejne liczby z listy, które są malejące.
# Dany element listy może być ponownie wykorzystany.
# np. lista = [5,4,3,2,1] to mamy tutaj trzy trójki liczb [5,4,3], [4,3,2] oraz [3,2,1], które są rozwiązaniem.
for i in range(0,len(lista)-3):
    if lista[i]>lista[i+1] and lista[i+1]>lista[i+2]:
        print(lista[i:i+3])