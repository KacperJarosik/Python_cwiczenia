# 5. Losujemy liczby od 1-100 i po ilu losowaniach suma wyrzuconych wartości
#    tylko liczb parzystych będzie nie większa od wartości podanej jako parametr funkcji
#    count_random_even_numbers(sum_max).
import random
def count_random_even_numbers(sum_max):
    sum=0
    acount=0
    while True:
        acount=acount+1
        x = random.randint(1, 100)
        if x%2==0:
            sum=sum+x
        if sum > sum_max:
            return acount-1
if __name__ == '__main__':
    sum_max = int(input('Podaj maksymalna wartosc wylosowanych liczb parzystych: '))
    print('Po ',count_random_even_numbers(sum_max),'losowaniach suma wyrzuconych wartości tylko liczb parzystych nie jest większa od wartości podanej jako parametr funkcji')
