# 12. Wykorzystaj funkcję sorted do sortowania listy z wyrazami
#  względem długości stringu.
if __name__ == '__main__':
    lista = ['xd', 'lupa', 'zupa', 'mlekołaki', 'wilki', 'malezuki']
    lista.sort(key=len)
    print(lista)
