#!/usr/bin/env python
from matplotlib import pyplot
import numpy

x = numpy.linspace(0, 6, num=100)
y = lambda x: 8. - 29./6.*x + 5./6.*x*x
fig = pyplot.figure(figsize=(6,3), dpi=300, tight_layout=True)
ax = fig.add_subplot(111, ylim=[0,8])
ax.grid(True, color=[0.7]*3)
ax.plot(x, y(x))
fig.savefig('fem_example.png')
