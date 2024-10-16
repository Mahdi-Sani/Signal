import numpy as np
import matplotlib.pyplot as plt

# Define parameters
a = 0.8  # You can change the value of 'a' to see the effect
n = np.arange(-10, 20, 1)  # Range of n

# Define h[n] = (-a)^n * u[n], where u[n] is 1 for n >= 0
h_n = ((-a) ** n) * (n >= 0)  # u[n] is 1 for n >= 0

# Plot h[n] using plot instead of stem
plt.figure(figsize=(10, 6))
plt.plot(n, h_n, 'bo-', label=f'h[n] = (-{a})^n * u[n]', markersize=5)
plt.title(f"Impulse Response h[n] for a = {a}")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)
plt.axvline(0, color='k', linestyle='--')  # Show n=0 line
plt.legend()
plt.show()

# Causality
is_causal = np.all(h_n[n < 0] == 0)  # h[n] is zero for n < 0
print(f'Causal: {"Yes" if is_causal else "No"}')

# Memory
# If h[n] depends on past or future values, it has memory
has_memory = "Yes" if a != 0 else "No"
print(f'Memory: {has_memory}')

# Stability
# A system is stable if the sum of the absolute values of h[n] is finite
stable = np.sum(np.abs(h_n)) < np.inf  # Summing the absolute values to check
print(f'Stable: {"Yes" if stable else "No"}')
