import numpy as np
import fclock as fc

# Harmonograph parameters
# See: https://en.wikipedia.org/wiki/Harmonograph

T = 14*np.pi
n = 1000                          # Number of points to use
A = [2, 6, 1.2, 3]                # Amplitudes
f = [2, 6, 1, 2]                  # Frequencies
p = [np.pi/16, np.pi/2, np.pi/16, np.pi]    # Phase shifts
d = np.array([0.02, 0.0315, 0.02, 0.02])  # Exponential decay rate

# Generate input series
theta = np.linspace(1/n, T, num=n)
x = (A[0] * np.sin(f[0]*theta + p[0])*np.exp(-d[0]*theta) +
     A[1] * np.sin(f[1]*theta + p[1])*np.exp(-d[1]*theta))
y = (A[2] * np.sin(f[2]*theta + p[2])*np.exp(-d[2]*theta) +
     A[3] * np.sin(f[3]*theta + p[3])*np.exp(-d[3]*theta))

# Calculate fft series matrix
S = fc.get_fft(x, y)

# Animate the result
fc.animate_fclock(S, x, y, 'fig/harmonograph.gif')
