# Rysowanie diagramu z ilością ocen 2,2.5,3,3.5,4,4.5,5 z kolokwium
# z pliku zewnętrznego (na początku z listy)
import numpy
import matplotlib.pyplot

import matplotlib.pyplot as pyplot
if __name__ == "__main__":
    names = ['2', '2.5', '3', '3.5', '4', '4.5', '5']
    f = open("oceny.txt", "r")
    m = f.readline()
    m = m.split()
    for k in range(len(m)):
        m[k]=float(m[k])
    x1 = m.count(2.0)
    x2 = m.count(2.5)
    x3 = m.count(3.0)
    x4 = m.count(3.5)
    x5 = m.count(4.0)
    x6 = m.count(4.5)
    x7 = m.count(5.0)
    values = [x1, x2, x3, x4, x5, x6, x7]
    pyplot.bar(names, values)
    pyplot.scatter(names, values)
    pyplot.plot(names, values)
    pyplot.show()
