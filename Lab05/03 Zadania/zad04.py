# 4. Dana jest lista (można dodać dowolną o dowolnej liczbie elementów):
lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3,1, 19, 71, 21]
# Znajdz wszystkie trzy kolejne liczby z listy, które są malejące.
# W naszym przypadku są następujące trójki liczby:
# 24, 4, 2
# 5, 3, ,1
# Jeżeli dana trójka liczba jest już wykorzystana, to idziemy dalej i dany element listy nie może być już wykorzystany
# np. lista = [5,4,3,2,1] to mamy tylko jedną trójkę liczb [5,4,3] - trójka liczb  [4,3,2] oraz [3,2,1] nie są rozwiązaniem.
i=0
while i<len(lista)-3:
    if lista[i]>lista[i+1] and lista[i+1]>lista[i+2]:
        print(lista[i:i+3])
        i+=3
    else:
        i+=1