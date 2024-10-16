import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define parameters
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads
t = np.linspace(0, 0.01, 1000)  # Time range

# Define the impulse response h(t)
h_t = (1 / (R * C)) * np.exp(-t / (R * C))

# Define the input signal x(t) as a unit step function
x_t = np.ones_like(t)  # x(t) = u(t), unit step input

# Perform the convolution of x(t) and h(t) to get the output y(t)
y_t = np.convolve(x_t, h_t, mode='same') * (t[1] - t[0])  # Discrete convolution

# Plot the input, impulse response, and output
plt.figure(figsize=(10, 6))

# Plot impulse response h(t)
plt.subplot(3, 1, 1)
plt.plot(t, h_t)
plt.title('Impulse Response h(t)')
plt.xlabel('Time [s]')
plt.ylabel('h(t)')
plt.grid(True)

# Plot input signal x(t)
plt.subplot(3, 1, 2)
plt.plot(t, x_t)
plt.title('Input Signal x(t)')
plt.xlabel('Time [s]')
plt.ylabel('x(t)')
plt.grid(True)

# Plot output signal y(t)
plt.subplot(3, 1, 3)
plt.plot(t, y_t)
plt.title('Output Signal y(t)')
plt.xlabel('Time [s]')
plt.ylabel('y(t)')
plt.grid(True)

plt.tight_layout()
plt.show()
