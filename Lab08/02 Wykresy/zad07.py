# Rysowanie funkcji sinx, cosx, sin2x, cos2x na czterech wykresach
# w jednym oknie w dowolnej konfiguracji
import matplotlib.pyplot as pyplot
import pylab
x = pylab.arange(0.0, 4*pylab.pi, 0.01)
y1 = pylab.cos(x)
y2 = pylab.sin(x)
y3 = pylab.cos(2*x)
y4 = pylab.sin(2*x)
pyplot.subplot(224)
pylab.plot(x, y1,'-')
pyplot.subplot(223)
pylab.plot(x, y2,'-')
pyplot.subplot(222)
pylab.plot(x, y3,'-')
pyplot.subplot(221)
pylab.plot(x, y4,'-')
pyplot.show()