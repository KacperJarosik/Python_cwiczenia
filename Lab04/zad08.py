# 8. Liczymy całkę z funkcji podanej na stałe np. y = 2*x**2+x-6 lub y = sin x.
#    Podajemy jednoczesnie wartość x początkową, wartość x końcową i krok całkowania.
#    Sprawdzić różnicę przy podaniu różnych kroków całkowania.
#y=2*x*x+x-6
if __name__ == '__main__':
    print('Podaj wartosc początkową,końcową i krok całkowania w formacie: \nxp\nxk \nn')
    xp=float(input())
    xk=float(input())
    n=int(input())
    s=0
    dx=(xk-xp)/n
    for k in range (1,n):
        s=s+(xp+k*dx)
    s=s*dx
    print(s)