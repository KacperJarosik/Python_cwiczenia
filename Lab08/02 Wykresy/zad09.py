# Narysuj funkcję cos(2*pi*x) oraz cos(2*pi*x)*exp(x) na jednym wykresie
# dla x z zakresu <0, 2*pi>
import matplotlib
import math
import matplotlib.pyplot as pyplot
import pylab
x = pylab.arange(0.0, 2*pylab.pi, 0.01)
y1 = pylab.cos(2*pylab.pi*x)
y2=math.exp(x)
y2 *= pylab.cos(2*pylab.pi*x)
pylab.plot(x, y1,'-')
pylab.plot(x, y2,'-')
pyplot.show()