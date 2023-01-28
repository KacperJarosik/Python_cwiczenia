# Rysujemy funkcję f(x) = 1/(x+1) z wybranego zakresu,
# który przynajmniej obejmuję zakres x (-5,5) oraz y (-10,10). Uwaga na wartość x = -1.
import numpy
import matplotlib.pyplot

if __name__ == "__main__":
    x = numpy.linspace(-5, 5, 1000)
    y = 1 / x
    x[abs(y) > 10] = numpy.NaN
    label = r'$y=\frac{1}{x}$'
    matplotlib.pyplot.plot(x, y, label=label)
    matplotlib.pyplot.plot([0, 0], [-10, 10], '--')
    matplotlib.pyplot.plot([-5, 5], [0, 0], '--')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()
