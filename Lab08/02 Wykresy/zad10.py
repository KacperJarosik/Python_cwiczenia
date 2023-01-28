# wygeneruj pary liczb całkowitych x i y losowo z zakresu x (0,100) y (0,100)
# i przedstaw w postaci punktów rozkład tych punktów na płaszczyźnie x,y.
import matplotlib.pyplot as pyplot
import pylab
import random
x = random.randint(0,100)
y1 = random.randint(0,100)
pylab.plot(x, y1)
pyplot.show()