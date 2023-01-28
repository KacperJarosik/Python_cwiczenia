# Narysuj dwa osobne wykresy sin i cos (2 okresy)
import pylab as p
x = p.arange(0.0, 4*p.pi, 0.01)
y1 = p.cos(x)
y2 = p.sin(x)
p.plot(x, y1, 'r')
p.show()
p.plot(x, y2, 'b')
p.show()