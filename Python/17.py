import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define parameters
a = -0.5  # You can change this value to see the effect of different 'a'
t = np.linspace(-5, 10, 1000)  # Time range

# Define h(t) = exp(at) * u(t)
h_t = np.exp(a * t) * (t >= 0)  # u(t) is 1 for t >= 0

# Plot h(t)
plt.figure(figsize=(10, 6))
plt.plot(t, h_t, label=f'h(t) = exp({a}t)u(t)')
plt.title("Impulse Response h(t)")
plt.xlabel("Time t")
plt.ylabel("h(t)")
plt.grid(True)
plt.axvline(0, color='k', linestyle='--')  # Show t=0 line
plt.legend()
plt.show()

# Causality
is_causal = np.all(h_t[t < 0] == 0)  # h(t) is zero for t < 0
print(f'Causal: {"Yes" if is_causal else "No"}')

# Memory
# If h(t) depends on past or future values, it has memory
has_memory = "Yes" if a != 0 else "No"
print(f'Memory: {has_memory}')

# Stability
# A system is stable if the integral of the absolute value of h(t) is finite
stable = np.trapz(np.abs(h_t), t) < np.inf  # Integrating over time to check
print(f'Stable: {"Yes" if stable else "No"}')
