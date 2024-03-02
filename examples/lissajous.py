import numpy as np
import fclock as fc

# Lissajous Curve parameters
# See: https://en.wikipedia.org/wiki/Lissajous_curve
# The appearance is highly sensitive to the ratio a/b

n = 500         # Number of points to use
A = 3           # x amplitude
B = 3           # y amplitude
a = 1           # x frequency
b = 3           # y frequency
delta = np.pi/2

# Generate input series
theta = np.linspace(1/n, 2*np.pi, num=n)
x = A * np.sin(a*theta + delta)
y = B * np.sin(b*theta)

# Calculate fft series matrix
S = fc.get_fft(x, y)

# Animate the result
fc.animate_fclock(S, x, y, 'fig/lissajous.gif')
